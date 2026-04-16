DATABASE = []
def cadastrar():
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

def excluir():
    global DATABASE
    e = input('nome do cliente:')
    for i in DATABASE:
        if i['nome'] == e:
            DATABASE.remove(i)
            print('Removido com sucesso',DATABASE)

def main():
    while True:
        print('1-cadastrar')
        print('2-ver usuario')
        print('3- excluir')
        print('4-sair')
        try:
            a = int(input('Escolha uma opcao: '))
        except ValueError:
            print('Apenas numeros.')
            continue
        if a ==1:
            cadastrar()
        elif a ==2:
            print(DATABASE)
        elif a ==3:
            excluir()
        elif a ==4:
            print('saindo')
            break
        else:
            print('opcao invalida')
main()

