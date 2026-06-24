import pandas as pd

df_notas = pd.read_excel("Automacao-3InfoB\\aula10\\notas_estudantes.xlsx", sheet_name="Notas")
df_atividades = pd.read_excel("Automacao-3InfoB\\aula10\\notas_estudantes.xlsx", sheet_name="Atividades")

print("DF Notas")
print(df_notas)
print("\nDF Atividades")
print(df_atividades)

df_notas.loc[len(df_notas)] = ["Lucas Silva", "Prova Final", 8.5]

print("\nLucas Silva adicionado")
print(df_notas)

df_notas.loc[(df_notas["Nome"] == "Ana Souza") & (df_notas["Atividade"] == "Trabalho 1"), "Nota"] = 9.0

print("\nAna Souza atualizada")
print(df_notas)

df_notas = df_notas[~((df_notas["Nome"] == "Pedro Santos") & (df_notas["Atividade"] == "Prova 1"))]

print("\nPedro Santos (Prova 1) excluido")
print(df_notas)

notas_maiores_7 = df_notas[df_notas["Nota"] > 7.0]
print("\nNota maior que 7")
print(notas_maiores_7)

media_por_estudante = df_notas.groupby("Nome")["Nota"].mean().reset_index()
media_por_estudante.columns = ["Nome", "Média das Notas"]
print("\nMédia das notas por estudante")
print(media_por_estudante)

nome_nota = df_notas[["Nome", "Nota"]]
print("\nApenas as colunas Nome e Nota")
print(nome_nota)

prova_final = df_notas[df_notas["Atividade"] == "Prova Final"]
print("\nProva Final")
print(prova_final)

nome_atividade_nota_alta = df_notas[df_notas['Nota'] > 7.0][['Nome', 'Atividade']]
print("\nNome e Atividade de estudantes com nota maior que 7.0")
print(nome_atividade_nota_alta)

df_ordenado = df_notas.sort_values('Nome', ascending=True).reset_index(drop=True)
print("\nDataFrame ordenado por ordem alfabetica")
print(df_ordenado)

df_combinado = pd.merge(df_notas, df_atividades, on='Atividade', how='left')
print("\nDataFrame combinado")
print(df_combinado)

df_ordenado.to_excel("notas_estudantes_ordenado.xlsx", index=False)