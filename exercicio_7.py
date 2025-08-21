# Solicitação de nome

nome = input("Informe seu primeiro nome:") 


# verificação de nome curto, normal ou muito grande.

if len(nome) < 6:
    print(f"Olá {nome} seu nome é curto.")
elif len(nome) == 6:
    print(f"Olá {nome} seu nome é normal.")
else:
     print(f"Olá {nome} seu nome é muito grande.")