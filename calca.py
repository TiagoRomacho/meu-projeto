def calculadora():
    print("Calculadora Simples - Soma, Subtração e Multiplicação")
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *): ")
    num2 = float(input("Digite o segundo número: "))

    if operacao == '+':
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif operacao == '-':
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif operacao == '*':
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    else:
        print("Operação inválida. Use +, - ou *.")

calculadora()

