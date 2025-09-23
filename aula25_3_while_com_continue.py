'''
Nesta aula é apresentado o continue 
que ajuda a pular uma parte do codigo 

'''
contador = 0

while contador <= 100:
    contador += 1

    if contador == 5:
        print(f'Não vou mostrar o', contador)
        continue
    if contador >= 10 and contador <= 30:
        print(f'Não vou mostrar',contador)
        continue
   
    print(contador)


