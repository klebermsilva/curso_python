# Nesta  parte do programa será solicitado ao usuário um número inteiro 

inteiro = input("Informe um número inteiro? ")


# Verificação se o valor émpar ou Par 



if inteiro.isdigit():
   numero = int(inteiro)
   if numero % 2 == 0:
      print(f"O valor informado {numero} e ele é Par")
   else:
      print(f"O valor informado {numero} e ele é Impar")
else:
   print("Você não digitou um número inteiro")



