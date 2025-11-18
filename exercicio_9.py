# Calculadora simples em Python
print("Bem-vindo à calculadora simples!")
print("*"*50)
print("Digite os números desejados para calcular.")


# ------------------------------------------------------------------------------

valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))

print("Escolha uma opção:\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Sair\n")
opcao = input("Digite a opção desejada (1/2/3/4/5): ")

# ------------------------------------------------------------------------------

while opcao == '1':
    resultado = valor_1 + valor_2
    print(f"O resultado da adição é: {resultado:.0f}")
    break
while opcao == '2':
    resultado = valor_1 - valor_2
    print(f"O resultado da subtração é: {resultado:.0f}")
    break
while opcao == '3':
    resultado = valor_1 * valor_2
    print(f"O resultado da multiplicação é: {resultado:.0f}")
    break
while opcao == '4':
    resultado = valor_1 / valor_2
    print(f"O resultado da divisão é: {resultado:.0f}")
    break
while opcao == '5':
    print("Saindo da calculadora. Até mais!")
    break


