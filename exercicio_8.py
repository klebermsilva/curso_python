# Solicita ao usuário que insira o seu nome
nome = input("Digite o seu nome: ")

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra + '*'
    indice += 1

print(f'{len(nome)}\n{novo_nome}\n{len(novo_nome)}')
    