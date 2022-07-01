def computador_escolhe_jogada(n,m):
    tira = n % (m+1)
    print("O computador tirou", tira,"peças")
    if n - tira == 0:
        print("Fim do jogo! O computador ganhou!")
    else:
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            print("Agora restam apenas", (n-tira), "peças no tabuleiro.")
            print()
    return tira

def usuario_escolhe_jogada(n,m):
    
    tira = int(input("Quantas peças você vai tirar?"))
    while tira < 0 or tira > m:
        print("Oops! Jogada inválida! Tente de novo.")

        tira = int(input("Quantas peças você vai tirar?"))
    print("Você tirou", tira, "peças.")
    if n - tira == 0:
        print("Fim do jogo! Você ganhou!")
    else:
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            print("Agora restam apenas", (n-tira), "peças no tabuleiro.")
            print()
    return tira

def partida():
    print()
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()
    if n % (m+1) == 0:
        print("Você começa!")
        while n > 0:
            n = n - usuario_escolhe_jogada(n,m)
            n = n - computador_escolhe_jogada(n,m)

    else:
        print("Computador começa!")
        while n > 0:
            n = n - computador_escolhe_jogada(n,m)
            if n > 0:
                n = n - usuario_escolhe_jogada(n,m)

def campeonato():
    print()
    pontos_computador = 0
    pontos_usuario = 0
    i = 1
    while i <= 3:
        print("**** Rodada", i," *****")
        print()
        i = i + 1
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        print()
        if n % (m+1) == 0:
            print("Você começa!")
            print()
            while n >0:
                n = - usuario_escolhe_jogada(n,m)
                if n == 0:
                    pontos_usuario = pontos_usuario + 1
                n = n - computador_escolhe_jogada(n,m)
                if n == 0:
                    pontos_computador = pontos_computador +1

        else:
            print("Computador começa!")
            print()
            while n > 0:
                n = n - computador_escolhe_jogada(n,m)
                print()
                if n == 0:
                    pontos_computador = pontos_computador + 1
                if n > 0:
                    n = n - usuario_escolhe_jogada(n,m)
                    print()
                    if n == 0:
                        pontos_usuario = pontos_usuario +1
    
    print("**** Final do campeonato! ****")
    print("Placar: Você", pontos_usuario, "X",pontos_computador,"Computador" )
          
    

print("Bem-vindo ao jogo NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
tipo = input("2 - para jogar um campeonato ")

if tipo == "1":
    partida()
else:
    if tipo == "2":
        campeonato()

