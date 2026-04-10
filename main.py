tabuleiro = [' '] * 9
escolha = input('Escolha X ou O para comecar o jogo: ').upper()
jogadordavez = escolha
def exibir_tabuleiro():
    print(f'{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
    print('---------')
    print(f'{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
    print('---------')
    print(f'{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}')

def obter_jogada():
    while True:
        try:
            jogada = int(input(f'Jogador: {jogadordavez} Escolha uma Jogada: '))
        except ValueError:
            print('Apenas numeros.')
            continue
        if jogada < 0 or jogada > 8:
            print('Só os numeros 0 e 8.')
            continue
        if tabuleiro[jogada] != ' ':
            print('Casa está marcada,tente uma casa livre.')
            continue
        return jogada
    
def ganhador():
    vitoria =[(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a,b,c in vitoria:
        if tabuleiro[a] == jogadordavez and tabuleiro[b] == jogadordavez and tabuleiro[c] == jogadordavez:
            return True
    return False

def main():
    global jogadordavez
    while True:
        exibir_tabuleiro()
        jogada = obter_jogada()
        tabuleiro[jogada] = jogadordavez
        if ganhador():
            exibir_tabuleiro()
            print(f'O jogador:{jogadordavez} Ganhou !!')
            break
        if ' ' not in tabuleiro:
            exibir_tabuleiro()
            print('Empate,Tabuleiro preenchido.')
            break
        if jogadordavez == 'O':
            jogadordavez = 'X'
        else:
            jogadordavez = 'O'
main()



        
        
