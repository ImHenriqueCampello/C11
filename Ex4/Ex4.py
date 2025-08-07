print('Qual distancia da viagem: ')
distancia = float(input())

if distancia <= 200:
    preco = distancia * 0.50
    print(preco, ' R$')
else:
    preco = distancia * 0.45
    print(preco, 'R$')