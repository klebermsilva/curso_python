'''
Explicação sobre outro iterador em Python: o for com a função range().

A função range() é usada para gerar uma sequência de números inteiros.
Ela é frequentemente usada em loops for quando você precisa repetir uma ação um número específico de vezes.
Exemplo:
for i in range(5):
    print(i)
Isso imprimirá os números de 0 a 4.
'''

numero = range(11)

valor_fornecido = int(input('Digite um número para ver a tabuada: '))

for valor in numero:

    print(f'{valor_fornecido} X {valor} = {valor * valor_fornecido}')