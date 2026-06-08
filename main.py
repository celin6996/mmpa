import pygame
import sys
import random

LARGURA = 800
ALTURA = 600
TAMANHO_BLOCO = 20
FPS = 15 

COR_FUNDO = (30, 30, 30)       
COR_ARANHA = (100, 50, 150)    
COR_INSETO = (255, 69, 0)      

def inicializar():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Spider Grow - Protótipo Semana 2")
    relogio = pygame.time.Clock()
    return tela, relogio

def processar_eventos(direcao_atual):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direcao_atual != "BAIXO":
                return "CIMA"
            elif event.key == pygame.K_DOWN and direcao_atual != "CIMA":
                return "BAIXO"
            elif event.key == pygame.K_LEFT and direcao_atual != "DIREITA":
                return "ESQUERDA"
            elif event.key == pygame.K_RIGHT and direcao_atual != "ESQUERDA":
                return "DIREITA"
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    return direcao_atual

def atualizar_posicao(pos_x, pos_y, direcao):
    if direcao == "CIMA":
        pos_y -= TAMANHO_BLOCO
    elif direcao == "BAIXO":
        pos_y += TAMANHO_BLOCO
    elif direcao == "ESQUERDA":
        pos_x -= TAMANHO_BLOCO
    elif direcao == "DIREITA":
        pos_x += TAMANHO_BLOCO
    return pos_x, pos_y

def desenhar_tela(tela, aranha_x, aranha_y, inseto_x, inseto_y):
    tela.fill(COR_FUNDO) 
    pygame.draw.rect(tela, COR_ARANHA, (aranha_x, aranha_y, TAMANHO_BLOCO, TAMANHO_BLOCO))
    pygame.draw.rect(tela, COR_INSETO, (inseto_x, inseto_y, TAMANHO_BLOCO, TAMANHO_BLOCO))
    pygame.display.flip()

def executar_jogo():
    tela, relogio = inicializar()
    
    aranha_x = LARGURA // 2
    aranha_y = ALTURA // 2
    direcao = "DIREITA"
    
    inseto_x = random.randint(0, (LARGURA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
    inseto_y = random.randint(0, (ALTURA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
    
    while True:
        direcao = processar_eventos(direcao)
        aranha_x, aranha_y = atualizar_posicao(aranha_x, aranha_y, direcao)
        
        if abs(aranha_x - inseto_x) < TAMANHO_BLOCO and abs(aranha_y - inseto_y) < TAMANHO_BLOCO:
            inseto_x = random.randint(0, (LARGURA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
            inseto_y = random.randint(0, (ALTURA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
            
        desenhar_tela(tela, aranha_x, aranha_y, inseto_x, inseto_y)
        relogio.tick(FPS)

if __name__ == "__main__":
    executar_jogo()