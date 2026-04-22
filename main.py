escolha = input('Escolha X ou O para comecar o jogo: ').upper()
jogadordavez = escolha

def tamanhoTabuleiro():
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

def exibir_tabuleiro(tabuleiro,tamanho):
    for i in range(tamanho):
        iniciodacoisa = i * tamanho
        finaldacoisa = iniciodacoisa + tamanho
        linhas= tabuleiro[iniciodacoisa:finaldacoisa]
        print()

def obter_jogada():
    while True:
        try:
            jogada = int(input(f'Jogador: {jogadordavez} Escolha uma Jogada: '))
        except ValueError:
            print('Entrada invalida,Apenas Numeros.')
            continue
        if jogada < 0 or jogada > len(tabuleiro):
            print(f'So numeros entre 0 e {len(tabuleiro)-1}')
            continue
        if tabuleiro[jogada] != ' ':
            print('Casa está preenchida,Tente uma casa livre.')
            continue
        return jogada
    
def main():
    global jogadordavez,tabuleiro 
    tamanho = tamanhoTabuleiro()     
    tabuleiro = [' '] * (tamanho*tamanho)
    while True:
        exibir_tabuleiro(tabuleiro,tamanho)
        jogada = obter_jogada() 
        tabuleiro[jogada] = jogadordavez
        if ' ' not in tabuleiro:
            exibir_tabuleiro(tabuleiro,tamanho)
            print('Empate,tabuleiro completo deu Velha')
            break  
        if jogadordavez == 'X':
            jogadordavez = 'O'
        else:
            jogadordavez = 'X'
main()

