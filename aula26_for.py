"""
Nesta aula aprendemos sobre o laço de repetição for em Python.
O for é para iteraveis (como listas, tuplas, dicionários, conjuntos e strings).
"""
texto = "Python"

novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')