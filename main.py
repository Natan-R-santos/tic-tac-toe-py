escolha = input('Escolha X ou O para comecar o jogo: ').upper()
jogadordavez = escolha
def tamanhoTabuleiro():
    while True:
        try:
            i = int(input("Escolha um tamanho de tabuleiro: "))
        except ValueError:
            print("Entrada somente numeros!")
            continue
        if i < 3:
            print("Tamanho minimo é 3.")
        else:
            return i 

def criar_matriz(tamanho):
    tabuleiro=[]
    for _ in range(tamanho):
        linha=[" "] * tamanho
        tabuleiro.append(linha)
    return tabuleiro

def exibir_tabuleiro(tabuleiro):
    tamanho=len(tabuleiro)
    for i,linha in enumerate(tabuleiro):
        print(" | ".join(linha))
        if i < tamanho - 1:  # evita linha extra no final
            print('-' * (tamanho * 4 - 3))

def obter_jogada(tabuleiro):
    tamanho=len(tabuleiro)
    while True:
        try:
            linha=int(input(f"Jogador {jogadordavez} escolha uma linha: "))
            coluna=int(input(f"Jogador {jogadordavez} escolha uma coluna: "))
        except ValueError:
            print("Digite somente numeros amigo.")
            continue
        if linha < 0 or linha >= tamanho or coluna < 0 or coluna >= tamanho:
            print(f"Valores devem estar 0 e {tamanho-1}")
            continue
        if tabuleiro[linha][coluna] != " ":
            print("casa ocupada,tente outra livre.")
            continue
        return linha,coluna

def verificar_vitoria(tabuleiro,jogadordavez,linha,coluna):
    tamanho=len(tabuleiro)

    if all(tabuleiro[linha][coluna]==jogadordavez for coluna in range(tamanho)):
        return True
    if all(tabuleiro[linha][coluna]==jogadordavez for linha in range(tamanho)):
        return True
    if linha==coluna:
        if all(tabuleiro[i][i]==jogadordavez for i in range(tamanho)):
            return True
    return False

def main():
    global jogadordavez
    tamanho= tamanhoTabuleiro()
    tabuleiro = criar_matriz(tamanho)
    while True:
        exibir_tabuleiro(tabuleiro)
        linha,coluna=obter_jogada(tabuleiro)
        tabuleiro[linha][coluna]=jogadordavez
        if verificar_vitoria(tabuleiro,jogadordavez,linha,coluna):
            print(f"Jogador {jogadordavez} venceu !!")
            exibir_tabuleiro(tabuleiro)
            break
        if all(" " not in linha for linha in tabuleiro):
            print("Empate ninguem ganhou")
            exibir_tabuleiro(tabuleiro)
            break
        if jogadordavez == "X":
            jogadordavez="O"
        else:
            jogadordavez="X"
main()