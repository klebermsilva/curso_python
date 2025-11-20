# While/else


procurar = input("Digite o que procura no texto: ")

texto = "Python é uma linguagem de programação incrível"
i = 0
while i < len(texto):
    letra = texto[i]
    
    if letra == procurar:
        print(f"Encontrei o que procura no texto , na posição, {i}, letra {letra}")
        break
    i += 1
else:
    print("Não encontrei o que procura no texto")