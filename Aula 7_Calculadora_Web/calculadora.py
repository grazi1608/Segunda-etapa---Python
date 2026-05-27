import math
from flask import render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro"
            etapas = f"Erro: Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"
            
    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        num2 = float(num2_valor)

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"

        elif operacao == '-':
            resultado = num1 - num2
            etapas = f'{num1} - {num2} = {resultado}'

        elif operacao == '*':
            resultado = num1 * num2
            etapas = f'{num1} * {num2} = {resultado}'

        elif operacao == '/':
            if num2 != 0:
                resultado = num1 / num2
                etapas = f'{num1} / {num2} = {resultado}'
            else:
                resultado = "erro"
                etapas = "Erro: Divisão por zero não permitida."

        elif operacao == '**':
            resultado = num1 ** num2
            etapas = f'{num1} ** {num2} = {resultado}'

        elif operacao == "log":
            if num1 > 0 and num2 > 0 and num2 != 1:
                resultado = math.log(num1, num2)
                etapas = f'log de {num1} na base {num2} = {resultado}'
            else:
                resultado = "erro"
                etapas = "Erro: O logaritmando deve ser > 0 e a base deve ser > 0 e diferente de 1."

        else:
            resultado = 'operação inválida'
            etapas = 'operação selecionada é inválida'

    return render_template('calculadora.html', etapas=etapas, resultados=resultado)

       


