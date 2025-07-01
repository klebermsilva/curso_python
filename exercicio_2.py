# Neste exercicio foi proposto, saber o imc da pessa 

#--------------------------------------------------------------

'''
Este exercicio é composto por três partes solicitar os dados ao solicitante, 
calcular o peso / altura² para obter o IMC.
E por fim apresentar ao mesmo o resultado.

'''

#-------------------------------------------------------------------
      # ------------- Informações solicitadas -----------------

nome = input('Informe o seu nome: ')
sobrenome = input('Informe seu sobrenome: ')
peso = input('Informe seu peso: ')
altura = input('Informe a altura: ')

#------------------------------------------------------------------------
    # --------------- Conversão de Str para Float -----------------

conv_peso = float(peso)
conv_altura = float(altura)

#-----------------------------------------------------------------------
    #--------------------- Calculo ----------------------


imc = conv_peso / ( conv_altura * 2)
nome_compl = nome + ' ' + sobrenome 

#-------------------------------------------------------------------------
    # --------------------- Apresentando na tela ------------------


print(f' Olá! {nome_compl}  seu imc é de {:.2imc}
