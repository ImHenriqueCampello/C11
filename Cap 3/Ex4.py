alunos = [
    {'nome': 'Rick', 'Peso': 65},
    {'nome': 'Fabão', 'Peso': 80},
    {'nome': 'Dedé', 'Peso': 90}
]

mais_leve = alunos[0]
mais_pesado = alunos[0]

for aluno in alunos:
    if aluno['Peso'] < mais_leve['Peso']:
        mais_leve = aluno
    if aluno['Peso'] > mais_pesado['Peso']:
        mais_pesado = aluno

print(f"O mais leve é {mais_leve['nome']} com {mais_leve['Peso']} kg.")
print(f"O mais pesado é {mais_pesado['nome']} com {mais_pesado['Peso']} kg.")