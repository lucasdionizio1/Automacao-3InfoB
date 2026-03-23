n1 = float(input("Insira a nota 1: "))
n2 = float(input("Insira a nota 2: "))

m = (n1+n2)/2

if m>=6:
    print("\npabens paso\n")
else:
    ef = float(input("Insira a nota do Exame Final: "))
    mf = (ef+m)/2
    
    if mf>=6:
        print("\npabens paso\n")
    else:
        print("\npaso nao viu\n")