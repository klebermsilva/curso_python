'''
Tabuada com While e for 

'''

numero = int(input('Digite um número para ver a tabuada: '))
valor = 0

print(f'Tabuada do {numero} com while\n')
while valor < 11:
    print(f'{numero} X {valor} = {numero * valor}')
    valor += 1
print('-' * 20)



print(f'Tabuada do {numero} com for\n')
for valor in range(11):
    print(f'{numero} X {valor} = {numero * valor}')
print('\n')