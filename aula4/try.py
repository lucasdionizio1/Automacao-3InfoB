while True:
    try:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número:"))
        
        r = n1/n2
        print("Resultado da divisão:", r)
        break
    except ValueError:
        print("O valor digitado é inválido.\n")
    except ZeroDivisionError:
        print("Não pode dividir por 0.\n")
    except Exception as e:
        print("Ocorreu um erro:\n", e)