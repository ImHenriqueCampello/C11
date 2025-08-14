n = int(input("Quantas pessoas? "))

pessoas = []

for i in range(n):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")

    pessoa = {
        "nome": nome,
        "idade": idade,
        "sexo": sexo
    }
    pessoas.append(pessoa)

soma_idades = 0
for p in pessoas:
    soma_idades += p["idade"]
media_idade = soma_idades / n


mulheres_menos_20 = 0
for p in pessoas:
    if p["sexo"] == "F" and p["idade"] < 20:
        mulheres_menos_20 += 1

print("Média de idade do grupo: ", media_idade)
print("Mulheres com menos de 20 anos: ", mulheres_menos_20)
