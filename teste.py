DATABASE = []
def cadastro_usuario():
    nome = input('digite seu nome...')
    idade = int(input('digite sua idade...'))
    ativo = True
    user = {
        'nome': nome,
        'idade': idade,
        'ativo': ativo
    }
    DATABASE.append(user)
    print(DATABASE)
cadastro_usuario()