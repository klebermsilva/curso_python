'''
Como funciona o __iter_ e o _next_ em Python
'''

# texto = 'Python'.__iter__() # cria um iterador para o objeto
# print(texto)
# print(texto.__next__()) # Primeiro elemento
# print(texto.__next__()) # Segundo elemento
# print(texto.__next__()) # Terceiro elemento

'''
 Pode ser feito dos dois geitos 
'''


# ----------------------------------------------- #

# texto = iter('Python')

# print(next(texto)) # Primeiro elemento
# print(next(texto)) # Segundo elemento   


# ----------------------------------------------- #
'''
Isso que feito pelo for por baixo dos panos

'''
texto = 'Python'
interator = iter(texto)
while True:
    try:
        letra = next(interator)
        print(letra)
    except StopIteration:
        break


# ----------------------------------------------- #

print ('\n')

for letra in 'Python':
    print(letra)