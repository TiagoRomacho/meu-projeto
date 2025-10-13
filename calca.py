def calculadora():
    print("Calculadora Simples - Soma, Subtração, Multiplicação e Divisão")
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    #Realiza a operação escolhida#
    if operacao == '+':
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif operacao == '-':
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif operacao == '*':
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif operacao == '/':
        #Resolução da divisão por zero#
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Erro: divisão por zero não é permitida.")
    else:
        print("Operação inválida. Use +, -, * ou /.")

calculadora()
