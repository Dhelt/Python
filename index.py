with open('config.py') as c:
    exec(c.read())

print(text)
print('Bem vindo ao, KartDOCS')
print('Pressione a tecla ENTER para acessar a pagina de login')


while True:

    input('')

    os.system('cls')
    print(text)
    linha()
    user = input('Usuario: ')
    senha = input('Senha: ')

    linha()

    tempo()

    print('Aguarde um momento, {}... ' .format(user))

    tempo()

    os.system('cls')

    if verificar_login(user, senha):
        print("Senha Correta! Acessando painel...")
        tempo()

        os.system('cls')

        print(text)

        print('Confira seu documento abaixo:')

        with open('painel.py') as p:
            exec(p.read())


    else:
        print("Usuário ou senha incorretos.")
        linha()
        tempo()



