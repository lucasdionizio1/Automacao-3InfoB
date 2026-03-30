# While

continuar = True

while continuar:
    print("Digite o nome do aluno: ")
    aluno = input()
    
    # Ao invés de mudar o input pra int, dá pra fazer o if receber uma string "0"
    resp = int(input("Deseja continuar: \n0 para NÃO\n1 para SIM\nDigite aqui: "))
    if resp == 0:
        continuar = False