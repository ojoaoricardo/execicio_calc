# Calculadora simples em Python

# Mostra o menu
print("=== Calculadora Simples ===")
print("Operações disponíveis: +, -, *, /")

# Pede os números e a operação
num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

# Faz o cálculo
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Operação inválida!"

# Mostra o resultado
print("Resultado:", resultado)