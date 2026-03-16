tabuleiro = [' '] * 9
jogadordavez = 'O'
def exibir_tabuleiro():
    print(f'{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
    print('---------')
    print(f'{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
    print('---------')
    print(f'{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}')

def verificar_ganhador(tabuleiro,jogadordavez):
    vitorias = [
        (0,1,2),(3,4,5),(6,7,8),# combinador horizontal
        (0,3,6),(1,4,7),(2,5,8),# combinador vertical
        (0,4,8),(2,4,6)# combinador diagonal
    ]
    for a,b,c in vitorias:
        if tabuleiro[a] == jogadordavez and tabuleiro[b] == jogadordavez and tabuleiro[c]== jogadordavez:
            return True
    return False

while True:
    exibir_tabuleiro()
    jogada = int(input('Insira de 0 a 8:'))
    if tabuleiro[jogada] != ' ':
        print('CASA OCUPADA TENTE OUTRA')
        continue
    tabuleiro[jogada] = jogadordavez 
    if verificar_ganhador(tabuleiro,jogadordavez):
        exibir_tabuleiro()
        print(f'Jogador: {jogadordavez} Venceu')
        break
    if jogadordavez == 'O':
        jogadordavez = 'X'
    else:
        jogadordavez  ='O'
        
