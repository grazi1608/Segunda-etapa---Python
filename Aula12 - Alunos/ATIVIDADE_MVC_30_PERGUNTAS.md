# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: _______________________________
- Turma: _______________________________

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.

A pasta models.


**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?

O app.py, porque a partir deles conseguimos executar  e ver o projeto.

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?

ModeloBase - base.py
FilmeFavorito - filme_favorito.py
HistoricoBusca - historico_busca.py

  

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?

Eles vão herdar o modeloBase e a partir disso vão herdar id, data de atualização e data de criação.

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?

"filmes_favoritos", pra deixar o codigo mais fácil e organizado.

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?

  A coluna tmdb_id com as restrições unique e nullable.

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?

Adiciona um nomo registro no banco de dados que contém o id, titulo, poster, nota e ano.

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?

Está na pasta historico_busca.py na classe ultimas.

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.

 Só alguns campos espelhados.
 exemplos: Poster, nota, ano e titulo.

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?
As classes que são:
ModeloBase - base.py
FilmeFavorito - filme_favorito.py
HistoricoBusca - historico_busca.py
(porque é para ser assim)
---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).

Três Blueprints, sendo eles:
filmes_bp = Blueprint("filmes", __name__, url_prefix="/filmes")
dashboard_bp = Blueprint("dashboard", __name__)
favoritos_bp = Blueprint("favoritos", __name__, url_prefix="/favoritos")




**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?

Está na pasta filmes_controller.py e o nome da função é populares().

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).

Não entendi


**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?

        O controller que registra o termo no banco é o filmes_controller.py

          @classmethod
    def buscar_por_tmdb(cls, tmdb_id):
        return cls.query.filter_by(tmdb_id=tmdb_id).first()



**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?

O método post na url "/adicionar/<int:tmdb_id>"

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?
Acredito que não acontefce nada porque none significa nada

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).
No app.py
app.register_blueprint(dashboard_bp)
app.register_blueprint(filmes_bp)
app.register_blueprint(favoritos_bp)

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?

O controller favoritos_controller.py. Ele envia filme reente e histórico


**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?

Model, porque eu  não sei 

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.

request.form - usa o  GET 
request.args - utiliza o POST

A diferença é que o GET envia os parâmetros diretamente na URL (ficando visíveis),enquanto o POST envia as informações ocultas no corpo da requisição.


---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?

Ficam em favoritos e filmes. O caminho completo é H:\python\Aula12 - Alunos\views\templates

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?

O templete layout.html. Os  templates usam esse layout a partir do código

{% extends "layout.html" %}
{% block title %}StreamFlix — Onde assistir{% endblock %}

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.

<a class="nav-brand" href="{{ url_for('dashboard.index') }}">StreamFlix</a>
        <a href="{{ url_for('filmes.populares') }}">Populares</a>
        <a href="{{ url_for('filmes.melhores') }}">Melhores</a>
        <a href="{{ url_for('filmes.buscar') }}">Buscar</a>
        <a href="{{ url_for('favoritos.listar') }}">Favoritos</a>

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?

Dentro de filmes na pasta listar.html 

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado?um pedaço reutilizado e com qual tag Jinja?

Um um pedaço reutilizado reutilizado com a tag {% if filme.poster_url %}

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?

 {% if favorito %}
            <form method="POST" action="{{ url_for('favoritos.remover', tmdb_id=filme.id) }}">
                <input type="hidden" name="voltar" value="{{ url_for('filmes.detalhe', filme_id=filme.id) }}">
                <button type="submit" class="btn btn-outline">★ Remover dos favoritos</button>
            </form>




**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?

O css está no static

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.

{% if favoritos %}

filme 
nota 
ano

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?

Se tivber no modo demo só vai aparecer uma div falando que está desuatualizada.

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.

Depois de vc clicar em salvar no site -> vai pra controllers na parde adicionar e depois disso vai para model 

---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
