matrix = [[2,4, 2, 4], [2, 4, 2, 4], [2, 4, 2, 4], [2, 4, 0, 0]]
posicao = 0
historico_pontos=[]
pontos = 0
jogadas_validas = 0
jogo= True
lista= []
perdeu = False
import pyfiglet #biblioteca ultilisada para gerar fontes personalizadas
import random
import colorama
from colorama import Fore, Back, Style #biblioteca usada para colorir itens da matriz e outros prints
colorama.init()

def print_tabela():
    print(Fore.LIGHTBLUE_EX + "+" + "-" * 20 + "+" + "-" * 20 + "+" + "-" * 20 + "+" + "-" * 20 + "+")
    for i in range(4):
        for a in range(4):
            espaco ='        '
            if matrix[i][a] > 9:
                espaco = '       '
            if matrix[i][a] > 99:
                espaco = '      '
            if matrix[i][a] > 999:
                espaco = '     '
            print(Fore.LIGHTWHITE_EX + f'|',"        ", end=" ")  #funçao Fore é da biblioteca colored
            if matrix[i][a] == 0:
                print(Fore.RED + Style.BRIGHT + f'{matrix[i][a]}',end=espaco)
            if matrix[i][a] == 2:
                print(Fore.MAGENTA + Style.BRIGHT +  f'{matrix[i][a]}',end=espaco)
            if matrix[i][a] == 4:
                print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f'{matrix[i][a]}',end=espaco)
            if matrix[i][a] == 8:
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + f'{matrix[i][a]}',end=espaco)
            if matrix[i][a] == 16 or matrix[i][a] == 32:
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f'{matrix[i][a]}',end=espaco)
            if matrix[i][a] == 64 or matrix[i][a] == 128:
                print(Fore.BLUE + Style.BRIGHT + f'{matrix[i][a]}',end=espaco)
            if matrix[i][a] == 256 or matrix[i][a] == 512:
                print(Fore.LIGHTBLUE_EX + Style.BRIGHT + f'{matrix[i][a]}',end=espaco)
            if matrix[i][a] == 1024:
                print(Fore.CYAN + Style.BRIGHT + f'{matrix[i][a]}',end=espaco)
            if matrix[i][a] == 2048:
                print(Fore.LIGHTWHITE_EX + Style.BRIGHT + f'{matrix[i][a]}',end=espaco)
        print(Fore.LIGHTWHITE_EX + f'|', end="")
        print(espaco)
        print(Fore.LIGHTWHITE_EX + f"____"*21)
    print(Fore.LIGHTBLUE_EX + "+" + "-" * 20 + "+" + "-" * 20 + "+" + "-" * 20 + "+" + "-" *20 + "+")


def gerar_numero():
    # apenas aumenta a probabilidade de aparecer um 2 a um numero 4
    provavel = random.randrange(0, 4)
    if provavel >= 0 and provavel <= 3:
        numero_matrix = 2
    else:
        numero_matrix = 4

    linha_aleatorio = random.randrange(0, 4)
    coluna_aleatorio = random.randrange(0, 4)

    while matrix[linha_aleatorio][coluna_aleatorio] > 0: #o programa ira soterar posições no tabuleiro até encontrar uma posição vazia
        linha_aleatorio = random.randrange(0, 4)
        coluna_aleatorio = random.randrange(0, 4)

    matrix[linha_aleatorio][coluna_aleatorio] = numero_matrix


def direcao_cima(tabuleiro):
    global pontos
    global jogadas_validas
    mesclar = True
    cont = 0
    tab = 0
    tab2 = 0
    for linha in range(4):
        for coluna in range(4):
            mover = 0
            if linha > 0:
                for q in range(linha):
                    if tabuleiro[q][coluna] == 0:
                        mover += 1
                """este for foi usado para identificar quantas posições vasias estão acima de cada celula,
                 a iteração esta funcionando de cima para baixo, por exemplo se a posição 0 for vazia,
                  quer dizer que a posição 1 irá subir e assim em diante'"""

                if mover > 0:
                    tabuleiro[linha - mover][coluna] = tabuleiro[linha][coluna]
                    tabuleiro[linha][coluna] = 0

                if mesclar == True:
                    if tabuleiro[linha - mover - 1][coluna] == tabuleiro[linha - mover][coluna]: #se a posiçao acima da atual for igual a ela, então irá ocorrer a soma
                        cont += 1
                        tabuleiro[linha - mover - 1][coluna] *= 2
                        pontos += tabuleiro[linha - mover - 1][coluna]
                        tabuleiro[linha - mover][coluna] = 0
                        tab = tabuleiro[linha - mover - 1][coluna]
                        tab2 = tabuleiro[linha - mover][coluna]

    if cont > 0:
        mesclar = False
        cont = 0
        print("")
        print("----" * 10, end='')
        print('SCORE', end='')
        print('----' * 10)
        print(f'                                         {pontos}')
        print('---' * 28)

    if tab == tab2:
        jogadas_validas += 1

def direcao_baixo(tabela):
    global jogadas_validas
    global pontos
    mesclar = True
    cont = 0
    cont_ponto = 0
    tab = 0
    tab2 = 0
    for linha in range(3):  # o range se iniciou com 3, para desconsiderar a ultima posição da matriz
        for coluna in range(4):
            mover = 0
            for q in range(linha + 1):
                if tabela[3 - q][coluna] == 0: #o (3 -q), significa que a leitura da matriz sera feita de baixo para cima
                    mover += 1
            if mover > 0:
                tabela[2 - linha + mover][coluna] = tabela[2 - linha][coluna]
                tabela[2 - linha][coluna] = 0

            if mesclar == True:
                if 3 - linha + mover <= 3:  # isto foi preciso para evitar que o movimento ultrapasse o limete da matrix
                    if tabela[2 - linha + mover][coluna] == tabela[3 - linha + mover][coluna]:
                        tab = tabela[2 - linha + mover][coluna]
                        tab2 = tabela[3 - linha + mover][coluna]
                        tabela[3 - linha + mover][coluna] *= 2
                        cont += 1
                        pontos += tabela[3 - linha + mover][coluna]
                        tabela[2 - linha + mover][coluna] = 0

    if cont > 0:
        mesclar = False
        cont = 0
        print("")
        print("----" * 10, end='')
        print('SCORE', end='')
        print('----' * 10)
        print(f'                                         {pontos}')
        print('---' * 28)

    if tab == tab2 and tab > 0 and tab2 > 0:
        jogadas_validas += 1

""""" os movimentos da esquerda seguem o mesmo padrão logico da subida, 
a diferença esta na ultilização da variavel coluna para de referência  aos movimentos >>"""
def direcao_esquerda(tabuleiro):
    global pontos
    global jogadas_validas
    mesclar = True
    cont = 0
    tab = 0
    tab2 = 0
    for linha in range(4):
        for coluna in range(4):
            mover = 0
            for q in range(coluna):
                if tabuleiro[linha][q] == 0:
                    mover += 1

            if mover > 0:
                tabuleiro[linha][coluna - mover] = tabuleiro[linha][coluna]
                tabuleiro[linha][coluna] = 0

            if mesclar == True:
                if tabuleiro[linha][coluna - mover] == tabuleiro[linha][coluna - mover - 1] and tabuleiro[linha][coluna - mover] != 0 and  tabuleiro[linha][coluna - mover - 1] != 0 :
                    tabuleiro[linha][coluna - mover - 1] *= 2
                    tab = tabuleiro[linha][coluna - mover]
                    tab2 = tabuleiro[linha][coluna - mover - 1]
                    pontos += tabuleiro[linha][coluna - mover - 1]
                    tabuleiro[linha][coluna - mover] = 0
    if cont > 0:
        mesclar = False
        cont = 0
        print("")
        print("----" * 10, end='')
        print('SCORE', end='')
        print('----' * 10)
        print(f'                                         {pontos}')
        print('---' * 28)

    if tab == tab2 and tab > 0 and tab2 > 0:
        jogadas_validas += 1

def direcao_direita(tabuleiro):  # a direção para a direita segue a mesma logica da direção para baixo, apenas mudando o parametro para for in colunas
    global pontos
    global jogadas_validas
    mesclar = True
    cont = 0
    tab = 0
    tab2 = 0
    for linha in range(4):
        for coluna in range(4):
            mover = 0
            for q in range(coluna):
                if tabuleiro[linha][3 - q] == 0:
                    mover += 1
            if mover > 0:
                tabuleiro[linha][3 - coluna + mover] = tabuleiro[linha][3 - coluna]
                tabuleiro[linha][3 - coluna] = 0

            if mesclar == True:
                if 4 - coluna + mover <= 3:
                    if tabuleiro[linha][3 - coluna + mover] == tabuleiro[linha][4 - coluna + mover]:
                        tabuleiro[linha][4 - coluna + mover] *= 2
                        cont += 1
                        pontos += tabuleiro[linha][4 - coluna + mover]
                        tabuleiro[linha][3 - coluna + mover] = 0
    if cont > 0:
        mesclar = False
        cont = 0
        print("")
        print("----" * 10, end='')
        print('SCORE', end='')
        print('----' * 10)
        print(f'                                         {pontos}')
        print('---' * 28)

    if tab2 == tab and tab > 0 and tab2 > 0:
        jogadas_validas += 1

def vitoria(tabuleiro):
    global jogo
    for i in range(4):
        for j in range(4):
            lista.append(tabuleiro[i][j])
    if 2048 in lista:
        jogo = False
        fonte = "big"
        FONT = pyfiglet.Figlet(font=fonte) #função da biblioteca pyfiglet para aumentar fontes
        print(FONT.renderText("VOCE VENCEU !!"))
        print(Fore.LIGHTWHITE_EX + 20 * '-','SCORE', '-' * 30)
        print(pontos)
        print(20 * '-', 'JOGADAS VALIDAS', '-' * 20)
        print(jogadas_validas)
        print('---' * 19)

def derrota(tabuleiro):
    global jogo
    global perdeu
    for i in range(4):
        for j in range(4):
            lista.append(tabuleiro[i][j])
    if 0 not in lista:
        print(FONT.renderText("VOCE PERDEU \n 00 ( "))
        print('Histórico da partida')
        print(Fore.LIGHTWHITE_EX + 20 * '-', 'SCORE', '-' * 30)
        print(pontos)
        print(20 * '-', 'JOGADAS VALIDAS', '-' * 20)
        print(jogadas_validas)
        print('---' * 19)
        perdeu = True
    lista.clear()



fonte = 'big'
FONT = pyfiglet.Figlet(font=fonte)
print('''
''')
print(FONT.renderText("BEM  VINDO  \nAO  2048 ! !"))
gerar_numero()
gerar_numero()
print(Fore.LIGHTWHITE_EX + f'Regras do jogo: \nO jogo 2048 consiste na movimentação e soma de peças iguais até que seja formado um 2048\nPara  melhor experiência,jogue com o terminal totalmente aberto --)')
print('')
print('Para movimentar as peças ultilize:\n(w) para cima\n(s) para baixo\n(a) para a esquerda\n(d) para a direita')

while True:
        while jogo:
            print_tabela()
            move = input(Fore.LIGHTWHITE_EX + 'para qual direção deseja mover?')
            if move != 'w' and move != 's' and move != 'a' and move != 'd':
                print_tabela()
                move = input(Fore.LIGHTWHITE_EX + 'insira uma jogada valida:')
            else:
                if move == 'w':
                    direcao_cima(matrix)
                    gerar_numero()
                if move == 's':
                    direcao_baixo(matrix)
                    gerar_numero()
                if move == 'a':
                    direcao_esquerda(matrix)
                    gerar_numero()
                if move == 'd':
                    direcao_direita(matrix)
                    gerar_numero()
            vitoria(matrix)
            derrota(matrix)

            if perdeu == True:
                novamente = input(Fore.RED+'Deseja recomçar? responda com [s/n]')
                if novamente =="s":
                    jogadas_validas = 0
                    for i in range(4):
                        for j in range(4):
                               matrix[i][j] = 0
                               perdeu = False
                    gerar_numero()
                    gerar_numero()
                    historico_pontos.append(pontos)

                if novamente =="n":
                    print(Fore.LIGHTBLUE_EX + 'fim de jogo!')
                    jogo = False
                    break


