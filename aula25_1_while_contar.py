'''
Nesta aula será explicado melhor como 
funciona a repetição e como contar

'''
contador = 0
tabuada = int( input('Informe sua o valor da tabuada: '))


while (contador < 10 ):
    contador = contador + 1
    valor = (contador * tabuada)
    
    print(f'{tabuada} X {contador} = {valor}')
    