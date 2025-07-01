"""
  Nesta aula é mostrado as precedencias aquilo que será executoda 
  em sequencia: 1 - Parenteses, 2 - exponenciação, 3 - (multiplicação, divisão, divisão inteira, modulo), 4 - (adição, subtração)   
  
"""

#--------------------------------------------------------------------------------------------------------------------------------


# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)
