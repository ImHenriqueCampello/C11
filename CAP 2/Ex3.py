var = input('Qual o seu sexo (M ou F): ')

while var != 'M' and var != 'F':
    print("Entrada inválida. Digite apenas 'M' ou 'F'.")
    var = input()

if var == 'M':
    print('Masculino')
elif var == 'F':
    print('Femenino')

