'''
Nesta saberemo como utilizar o while dentro de outro 
while

'''

linhas = 5
colunas = 5 

linha = 1
while linha <= linhas:
    coluna = 1
    while coluna <= colunas:
        # imprime sem pular linha, adicionando espaços entre colunas
        print(f'{coluna} {linha}', end='   ')
        coluna += 1

    # depois de imprimir todas as colunas para esta linha, pula para a próxima
    print()
    linha += 1