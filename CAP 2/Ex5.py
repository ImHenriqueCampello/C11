x = int(input("Digite um número entre 1000 e 9999: "))

while x < 1000 or x > 9999:
    x = int(input("ENTRADA ERRADA, digite um número entre 1000 e 9999: "))

x_str = str(x)

print('Número do milhar:', x_str[0])
print('Número da centena:', x_str[1])
print('Número da dezena:', x_str[2])
print('Número da unidade:', x_str[3])
