#sf = situação final
aluno1 = {'nome':'Dedé','Idade':19, 'Nota': -10,'SF':'nada'}
aluno2 = {'nome':'Fabão','Idade':20, 'Nota': 9,'SF':'nada'}
aluno3 = {'nome':'Rick','Idade':22, 'Nota': 95,'SF':'nada'}
aluno4 = {'nome':'João Gabriel','Idade':19, 'Nota': 100,'SF':'nada'}

alunos = [aluno1,aluno2,aluno3,aluno4]

i = 0
for aluno in alunos:
    if alunos[i]['Nota'] >= 60:
        alunos[i]['SF'] = 'AP'
        i += 1
    else :
        alunos[i]['SF'] = 'RP'
        i += 1

print(alunos)




