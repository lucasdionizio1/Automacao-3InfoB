while True:
    usuD = input('Digite o usuário: ')
    senhaD = input('Digite a senha: ')
    if usuD == 'admin' and senhaD == 'admin123':
        print("Bem-vindo!")
        break
    else:
        print("Usuário ou senha incorretos!\n")