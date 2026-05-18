from flask import Flask # Letra minuscula no inicio e letra maiuscula no final

app = Flask(__name__) # inicio

@app.route('/decorator')
def decorator():
    return '''Um decorator é uma função que recebe outra função como argumento,\n  adiciona funcionalidades a ela e retorna essa nova função modificada. \n Ele permite que você altere o comportamento de uma função existente sem precisar modificar o código-fonte original. \n No Flask, o uso mais comum de um decorator é para vincular URLs (rotas) a funções específicas de visualização. \n O decorator @app.route avisa o Flask que, quando um usuário acessar uma determinada URL no navegador,\n  ele deve executar a função decorada.'''

if __name__ == '__main__':
   app.run(debug=True)
   