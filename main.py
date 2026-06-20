
import pygame
import sys
import random

LARGURA = 800
ALTURA = 600
TAMANHO = 20
FPS = 12

COR_FUNDO = (30,30,30)

def inicializar():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Spider Grow - Versão Final")
    return tela, pygame.time.Clock()

def processar_eventos(direcao):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direcao != "BAIXO": return "CIMA"
            if event.key == pygame.K_DOWN and direcao != "CIMA": return "BAIXO"
            if event.key == pygame.K_LEFT and direcao != "DIREITA": return "ESQUERDA"
            if event.key == pygame.K_RIGHT and direcao != "ESQUERDA": return "DIREITA"
    return direcao

def desenhar_aranha(tela, x, y):
    # aranha pixelada
    cor = (90,40,120)
    olho = (255,255,255)
    pixels = [
        (1,0),(2,0),(3,0),
        (0,1),(1,1),(2,1),(3,1),(4,1),
        (1,2),(2,2),(3,2),
        (0,3),(1,3),(3,3),(4,3)
    ]
    for px,py in pixels:
        pygame.draw.rect(tela, cor, (x+px*5,y+py*5,5,5))
    pygame.draw.rect(tela, olho,(x+7,y+7,3,3))
    pygame.draw.rect(tela, olho,(x+12,y+7,3,3))

def desenhar_inseto(tela,x,y):
    # inseto pixelado
    corpo=(220,80,20)
    asa=(120,180,255)
    pygame.draw.rect(tela, corpo,(x+7,y+5,8,12))
    pygame.draw.rect(tela, asa,(x,y+4,7,7))
    pygame.draw.rect(tela, asa,(x+15,y+4,7,7))
    pygame.draw.rect(tela, corpo,(x+5,y+17,3,3))
    pygame.draw.rect(tela, corpo,(x+15,y+17,3,3))

def atualizar_posicao(x,y,d):
    if d=="CIMA": y-=TAMANHO
    if d=="BAIXO": y+=TAMANHO
    if d=="ESQUERDA": x-=TAMANHO
    if d=="DIREITA": x+=TAMANHO
    return x,y

def executar_jogo():
    tela,relogio=inicializar()
    x,y=LARGURA//2,ALTURA//2
    direcao="DIREITA"
    vidas=3
    pontos=0

    inseto_x=random.randrange(0,LARGURA//TAMANHO)*TAMANHO
    inseto_y=random.randrange(0,ALTURA//TAMANHO)*TAMANHO

    fonte=pygame.font.Font(None,32)

    while True:
        direcao=processar_eventos(direcao)
        x,y=atualizar_posicao(x,y,direcao)

        if x<0 or x>=LARGURA or y<0 or y>=ALTURA:
            vidas-=1
            x,y=LARGURA//2,ALTURA//2

        if abs(x-inseto_x)<TAMANHO and abs(y-inseto_y)<TAMANHO:
            pontos+=1
            inseto_x=random.randrange(0,LARGURA//TAMANHO)*TAMANHO
            inseto_y=random.randrange(0,ALTURA//TAMANHO)*TAMANHO

        tela.fill(COR_FUNDO)
        desenhar_aranha(tela,x,y)
        desenhar_inseto(tela,inseto_x,inseto_y)

        texto=fonte.render(f"Vidas: {vidas}   Pontos: {pontos}",True,(255,255,255))
        tela.blit(texto,(10,10))

        if vidas<=0:
            fim=fonte.render("GAME OVER",True,(255,0,0))
            tela.blit(fim,(330,280))
            pygame.display.flip()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        relogio.tick(FPS)

if __name__=="__main__":
    executar_jogo()
