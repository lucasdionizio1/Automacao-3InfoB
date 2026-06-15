import pandas as pd

planilha = pd.read_excel("Automacao-3InfoB\\aula9\\Dados_3INFOB.xlsx")

planilha.loc[len(planilha)] = ["Pablo", 52, 1.8, "M"]

planilha.loc[16] = ["Pablo", 52, 1.8, "Masculino"]

planilha.loc[16, "Nome"] = "Pablo Sandi"

planilha.loc[16,]

print(planilha)