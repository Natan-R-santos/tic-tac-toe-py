def size_boards():
    while True:
        try:
            size = int(input("Digite o tamanho do tabuleiro (mínimo 3): "))
            if size < 3:
                print("Tamanho minimo é 3")
                continue
            if size > 10:
                print("Muito grande! Escolha um valor até 10.")
                continue
            return size
        except ValueError:
            print('Digite apenas números inteiros.')
size_boards()