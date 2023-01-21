import pgzrun

#Definindo variáveis globais
WIDTH = 300
HEIGHT = 300
GAME_OVER = False

#Definindo variáveis do nosso personagem
nave = Actor ('nave.png', (WIDTH/2, HEIGHT / 2))

#fUNÇÃO PARA DESENHAR A "TELA INICIAL" DO JOGO
def draw():
    # Por boa prática limpa a tela de jogo caso tenha lixo desenhado
    screen.clear()

    if GAME_OVER == False:

        # preenche a tela de branco
        screen.fill((255, 255, 255))

        # desenha a nave
        nave.draw()

    elif GAME_OVER == True:
        game_over()


def game_over():
    # Limpa a tela
    screen.clear()

    # Escreve alguma mensagem de GAME OVER
    screen.draw.text('GAME OVER!!', (70, 150))

#função chamada 1 vez por frame
def update():
    # retorna o angulo da nave para 0 graus
    nave.angle = 0

    # movimentação da nave
    if keyboard.left and GAME_OVER == False:
        nave.x -= 3
        nave.angle = 15
    elif keyboard.right and GAME_OVER == False:
        nave.x += 3
        nave.angle = 345
    if keyboard.up and GAME_OVER == False:
        nave.y -= 3
    elif keyboard.down and GAME_OVER == False:
        nave.y += 3


pgzrun.go()