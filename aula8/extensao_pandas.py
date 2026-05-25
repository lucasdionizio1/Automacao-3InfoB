import pandas as pd

planilha = pd.read_excel('Automacao-3InfoB\\aula8\\Alunos.xlsx')

print(planilha.loc[12])

print(planilha.loc[12, "Nome"])

print(planilha.loc[12, ["Nome", "Idade"]])

planilha.loc[12, "Nome"] = "Gabriela Pereira"
planilha.loc[12, ["Nome", "idade"]] = ["Gabriela Pereira de Souza", 20]

planilha.loc[len[planilha], ["Nome", "Idade"]] = ["Ivan", 40]

print(planilha)