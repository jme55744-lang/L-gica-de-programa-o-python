tabuleiro = [''for _ in range (9)]

def mostrar_tabuleiro():
    print(f"\n{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--|--|--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--|--|--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}\n")

def verificar_vitoria(tab, jogador):
    condicoes = [
        [tab[0], tab[1], tab[2]],    #linha 1
        [tab[3], tab[4], tab[5]],    #linha 2
        [tab[6], tab[7], tab[8]],   #linha 3
        [tab[0], tab[3], tab[6]],   #coluna 1
        [tab[1], tab[4], tab[7]],   #coluna 2
        [tab[2], tab[5], tab[8]],   #coluna 3
        [tab[0], [tab[4]], tab[8]],   #diagonal 1
        [tab[2], tab[4], tab[6]]   #diagonal 2
    ]
    return[jogador, jogador, jogador] in condicoes

def verificar_empate():
    return '' not in tabuleiro

def jogar():
    jogador_atual = 'X'
    while True:
        mostrar_tabuleiro()
        escolha = input(f"Vez do jogador {jogador_atual} escolha uma posição de 1 a 9: ")

        if escolha.isdigit() and 1 <= int(escolha) <= 9:
            posicao = int(escolha) - 1

            if tabuleiro[posicao] == " ":
                tabuleiro[posicao] = jogador_atual
            if verificar_vitoria(tabuleiro, jogador_atual):
                mostrar_tabuleiro()
                print( f"Parabéns o jogador {jogador_atual} venceu.")
                break
            if verificar_empate():
                mostrar_tabuleiro()
                print("Empate")
                break
            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Entrada inválida. Digite um número de 1 a 9.")

jogar()
