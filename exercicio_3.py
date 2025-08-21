#------------------------------------------------------------
# Este exercio é para treinar como realizar 
# comparação utilizando operadores logicos
#------------------------------------------------------------

    # Aqui começarei solicitando os números para comparação 
#-----------------------------------------------------------------

primeiro_valor = input('Informe o primeiro valor: ')
segundo_valor = input('Informe o segundo valor: ')

#------------------------------------------------------------------
    # Aqui será realizada a conversão dos valores
    #  de string para float  
#-------------------------------------------------------------------

conv_prim_valor = float(primeiro_valor)
conv_segun_valor = float(segundo_valor)

#--------------------------------------------------------------------#

            # Aqui começará a decisão com operadores # 
# -------------------------------------------------------------------#

if conv_prim_valor > conv_segun_valor:
    print(f'O número maior é {conv_prim_valor:.0f} e o  {conv_segun_valor:.0f} é o número menor ')
elif conv_segun_valor > conv_prim_valor:
   print(f'O número maior é {conv_segun_valor:.0f} e o  {conv_prim_valor:.0f} é o número menor ')
elif conv_prim_valor == conv_segun_valor:
    print(f'Não existe  maior ou menor  número {conv_prim_valor:.0f} eles são iguais {conv_segun_valor:.0f}')
else:
    print('O programa acabou!!!')