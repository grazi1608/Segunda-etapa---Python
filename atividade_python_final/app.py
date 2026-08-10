import sqlite3
import requests
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# 7. Segurança: Configuração de chave secreta
app.secret_key = "chave_secreta_super_segura_aqui"

DATABASE = "database.db"

# --- 2. Banco de dados ---
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    # Tabela de tarefas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT NOT NULL CHECK(status IN ('Pendente', 'Em andamento', 'Concluída')),
            usuario_id INTEGER NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        )
    ''')
    conn.commit()
    conn.close()

# Inicializa o banco ao rodar o script
init_db()


# --- 3. Autenticação ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        # Hash da senha com werkzeug.security
        senha_hash = generate_password_hash(senha)
        
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)',
                         (nome, email, senha_hash))
            conn.commit()
            flash('Cadastro realizado com sucesso! Faça login.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('E-mail já cadastrado.', 'danger')
        finally:
            conn.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM usuarios WHERE email = ?', (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user['senha'], senha):
            session['user_id'] = user['id']
            session['user_nome'] = user['nome']
            return redirect(url_for('dashboard'))
        else:
            flash('E-mail ou senha incorretos.', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Você saiu da conta.', 'info')
    return redirect(url_for('login'))


# --- 4 & 5. Dashboard, API Externa e CRUD ---
@app.route('/')
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']

    # 4. Consumo de API externa de frases motivacionais
    frase_motivacional = "Mantenha o foco e continue avançando!"
    try:
        response = requests.get('https://api.adviceslip.com/advice', timeout=3)
        if response.status_code == 200:
            frase_motivacional = response.json()['slip']['advice']
    except Exception:
        pass

    conn = get_db_connection()
    tarefas = conn.execute('SELECT * FROM tarefas WHERE usuario_id = ?', (user_id,)).fetchall()
    conn.close()

    return render_template('dashboard.html', tarefas=tarefas, frase=frase_motivacional)

@app.route('/nova_tarefa', methods=['GET', 'POST'])
def nova_tarefa():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        status = request.form['status']
        user_id = session['user_id']

        conn = get_db_connection()
        conn.execute('INSERT INTO tarefas (titulo, descricao, status, usuario_id) VALUES (?, ?, ?, ?)',
                     (titulo, descricao, status, user_id))
        conn.commit()
        conn.close()

        flash('Tarefa criada com sucesso!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('form_tarefa.html', modo='criar')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_tarefa(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    tarefa = conn.execute('SELECT * FROM tarefas WHERE id = ? AND usuario_id = ?', 
                           (id, session['user_id'])).fetchone()

    if not tarefa:
        conn.close()
        flash('Tarefa não encontrada.', 'danger')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        status = request.form['status']

        conn.execute('UPDATE tarefas SET titulo = ?, descricao = ?, status = ? WHERE id = ?',
                     (titulo, descricao, status, id))
        conn.commit()
        conn.close()

        flash('Tarefa atualizada com sucesso!', 'success')
        return redirect(url_for('dashboard'))

    conn.close()
    return render_template('form_tarefa.html', modo='editar', tarefa=tarefa)

@app.route('/excluir/<int:id>')
def excluir_tarefa(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    conn.execute('DELETE FROM tarefas WHERE id = ? AND usuario_id = ?', (id, session['user_id']))
    conn.commit()
    conn.close()

    flash('Tarefa excluída!', 'info')
    return redirect(url_for('dashboard'))


# --- 8. Endpoint API para Filtro por Status ---
@app.route('/api/tarefas')
def api_tarefas():
    if 'user_id' not in session:
        return jsonify({'error': 'Não autorizado'}), 401

    status_filtro = request.args.get('status', '')
    user_id = session['user_id']

    conn = get_db_connection()
    if status_filtro:
        query = 'SELECT * FROM tarefas WHERE usuario_id = ? AND status = ?'
        tarefas = conn.execute(query, (user_id, status_filtro)).fetchall()
    else:
        query = 'SELECT * FROM tarefas WHERE usuario_id = ?'
        tarefas = conn.execute(query, (user_id,)).fetchall()
    conn.close()

    resultado = [dict(t) for t in tarefas]
    return jsonify(resultado)


# --- 10. Dashboard de Progresso & Endpoint para Gráfico ---
@app.route('/progresso')
def progresso():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('progresso.html')

@app.route('/api/estatisticas_tarefas')
def estatisticas_tarefas():
    if 'user_id' not in session:
        return jsonify({'error': 'Não autorizado'}), 401

    user_id = session['user_id']
    conn = get_db_connection()
    
    pendentes = conn.execute("SELECT COUNT(*) FROM tarefas WHERE usuario_id = ? AND status = 'Pendente'", (user_id,)).fetchone()[0]
    andamento = conn.execute("SELECT COUNT(*) FROM tarefas WHERE usuario_id = ? AND status = 'Em andamento'", (user_id,)).fetchone()[0]
    concluidas = conn.execute("SELECT COUNT(*) FROM tarefas WHERE usuario_id = ? AND status = 'Concluída'", (user_id,)).fetchone()[0]
    conn.close()

    return jsonify({
        'Pendente': pendentes,
        'Em andamento': andamento,
        'Concluída': concluidas
    })


if __name__ == '__main__':
    # 7. DEBUG=False para ambiente de produção
    app.run(debug=True)