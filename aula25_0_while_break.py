''' 
O while repete o codigo em um laço infito 
a menos que, uma condição false sejá atribuida
ou coloque um break dentro do while

'''

usuario = 'Python_aula'
senha = 'Pyth@n3'

user = input('Informe o seu usuario cadastrado:')
passwoard = input('Informe a senha de cadastro:')

if usuario == user and senha == passwoard:
    while usuario and senha:
        print('Olá, bem vindo ao sistema!!!')
        break
else: 
    print('Usuario não encontrado')