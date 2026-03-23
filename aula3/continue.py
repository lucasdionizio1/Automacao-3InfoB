# dicionario
aluno1 = {"nome": "Pablo", "idade": 17, "sexo": "M"}
aluno2 = {"nome": "Carlos", "idade": 18, "sexo": "M"}
aluno3 = {"nome": "Samara", "idade": 17, "sexo": "F"}

# lista com dic
alunos = [aluno1, aluno2, aluno3]

# continue
for aluno in alunos:
    if aluno['idade'] >= 18:
        continue
    print("Olá", aluno['nome'], "qual é seu passa tempo")
    aluno['hobbie'] = input('')

print(alunos)