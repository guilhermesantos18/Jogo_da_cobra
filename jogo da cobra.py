import pygame
from pygame.locals import *  # importar todas as funções e todas as constantes
from sys import exit  # função para fechar a janela do jogo
from random import randint

pygame.init()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_1-up.wav')

vermelho = (255, 0, 0)
preto = (0, 0, 0)
azul = (0, 0, 255)
branco = (255, 255, 255)
verde = (0, 255, 0)

largura = 640
altura = 480
x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

speed = 5
velocidade_x = 0
velocidade_y = 0

x_maca = randint(30, 600)
y_maca = randint(30, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')
relogio = pygame.time.Clock()
tamanho_rect = 30
lista_cobra = []
comprimento_inicial = 1
morreu = False


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, verde, (XeY[0], XeY[1], tamanho_rect, tamanho_rect))


def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 1
    x_cobra = int(largura / 2)
    y_cobra = int(largura / 2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False


while True:
    relogio.tick(60)
    tela.fill(branco)
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, preto)
    for event in pygame.event.get():  # Verficar se o usuário apertou alguma tecla
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:  # Se eu apertei alguma tecla do teclado
            if event.key == pygame.K_LEFT and velocidade_x != 5:
                velocidade_y = 0
                velocidade_x = - speed
            if event.key == pygame.K_RIGHT and velocidade_x != -5:
                velocidade_y = 0
                velocidade_x = speed
            if event.key == pygame.K_UP and velocidade_y != 5:
                velocidade_x = 0
                velocidade_y = - speed
            if event.key == pygame.K_DOWN and velocidade_y != -5:
                velocidade_x = 0
                velocidade_y = speed

    x_cobra += velocidade_x
    y_cobra += velocidade_y

    cobra = pygame.draw.rect(tela, verde, (x_cobra, y_cobra, tamanho_rect, tamanho_rect))
    maca = pygame.draw.rect(tela, vermelho, (x_maca, y_maca, tamanho_rect, tamanho_rect))

    if cobra.colliderect(maca):
        x_maca = randint(30, 600)
        y_maca = randint(30, 430)
        comprimento_inicial += 5
        pontos += 1
        barulho_colisao.play()

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    print(lista_cobra.count(lista_cabeca))

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    if any(Bloco == lista_cabeca for Bloco in lista_cobra[
                                              :-1]):  # se tiver mais de uma lista igual a lista cabeça dentro da lista cobra quer dizer que a cobra encostostou nela mesma
        fonte2 = pygame.font.SysFont('arial', 20, True)
        print(lista_cobra.count(lista_cabeca))
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, preto)
        ret_texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            tela.fill(branco)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura // 2, altura // 2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    aumenta_cobra(lista_cobra)
    tela.blit(texto_formatado, (400, 40))
    pygame.display.update()
