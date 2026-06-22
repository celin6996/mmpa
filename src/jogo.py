import pygame
import sys
import random
import math

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    BRANCO,
    PRETO,
    CINZA,
    COR_TEIA,
    COR_TEIA_BRILHO,
    COR_FUNDO_TOPO,
    COR_FUNDO_BASE,
    TAMANHO_BLOCO,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
    mover_corpo,
    colidiu_com_proprio_corpo,
    calcular_tempo_decorrido,
    formatar_tempo,
)
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)

COR_ARANHA_CABECA = (180, 90, 220)
COR_ARANHA_CORPO = (120, 55, 160)
COR_ARANHA_OLHO = (255, 255, 255)
COR_INSETO = (255, 99, 40)
COR_INSETO_ASA = (130, 190, 255)


def inicializar():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
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

    
    pos_x = pos_x % LARGURA_TELA
    pos_y = pos_y % ALTURA_TELA

    return pos_x, pos_y


def gerar_posicao_inseto(corpo_aranha):
    
    colunas = LARGURA_TELA // TAMANHO_BLOCO
    linhas = ALTURA_TELA // TAMANHO_BLOCO

    while True:
        x = random.randrange(0, colunas) * TAMANHO_BLOCO
        y = random.randrange(0, linhas) * TAMANHO_BLOCO
        if (x, y) not in corpo_aranha:
            return x, y


def _construir_fundo_gradiente():
    
    fundo = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    for y in range(ALTURA_TELA):
        proporcao = y / ALTURA_TELA
        cor = [
            int(COR_FUNDO_TOPO[i] + (COR_FUNDO_BASE[i] - COR_FUNDO_TOPO[i]) * proporcao)
            for i in range(3)
        ]
        pygame.draw.line(fundo, cor, (0, y), (LARGURA_TELA, y))
    return fundo


def _construir_teia(pontos_brilho_seed):

    camada = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)

    cantos = [
        (40, 30),
        (LARGURA_TELA - 40, 30),
        (40, ALTURA_TELA - 30),
        (LARGURA_TELA - 40, ALTURA_TELA - 30),
        (LARGURA_TELA // 2, 10),
    ]

    for centro_x, centro_y in cantos:
        raio_max = 260
        num_raios = 9
        raios_pontas = []

        for i in range(num_raios):
            angulo = (2 * math.pi * i) / num_raios + 0.3
            fim_x = centro_x + raio_max * math.cos(angulo)
            fim_y = centro_y + raio_max * math.sin(angulo)
            raios_pontas.append((fim_x, fim_y))
            pygame.draw.aaline(camada, (*COR_TEIA, 130), (centro_x, centro_y), (fim_x, fim_y))

       
        num_espirais = 7
        for nivel in range(1, num_espirais + 1):
            fator = nivel / num_espirais
            pontos_anel = []
            for i in range(num_raios):
                angulo = (2 * math.pi * i) / num_raios + 0.3
                px = centro_x + raio_max * fator * math.cos(angulo)
                py = centro_y + raio_max * fator * math.sin(angulo)
                pontos_anel.append((px, py))
            pontos_anel.append(pontos_anel[0])
            pygame.draw.aalines(camada, (*COR_TEIA, 100), False, pontos_anel)


    rng = random.Random(pontos_brilho_seed)
    for _ in range(35):
        gx = rng.randint(20, LARGURA_TELA - 20)
        gy = rng.randint(20, ALTURA_TELA - 20)
        raio = rng.choice([1, 1, 2])
        alpha = rng.randint(60, 160)
        pygame.draw.circle(camada, (*COR_TEIA_BRILHO, alpha), (gx, gy), raio)

    return camada


def desenhar_cenario_teia(tela, fundo_cache, teia_cache):

    tela.blit(fundo_cache, (0, 0))
    tela.blit(teia_cache, (0, 0))


def desenhar_aranha(tela, corpo, direcao):
    
    total_segmentos = len(corpo)

    for indice, (seg_x, seg_y) in enumerate(corpo):
        eh_cabeca = indice == 0
        cor = COR_ARANHA_CABECA if eh_cabeca else COR_ARANHA_CORPO

        
        eh_traseira = indice >= total_segmentos - 2 and total_segmentos > 1
        tamanho = TAMANHO_BLOCO
        if eh_traseira:
            tamanho = int(TAMANHO_BLOCO * 1.15)

        offset = (TAMANHO_BLOCO - tamanho) // 2
        rect = pygame.Rect(seg_x + offset, seg_y + offset, tamanho, tamanho)

        if eh_traseira:
            pygame.draw.ellipse(tela, cor, rect)
        else:
            pygame.draw.rect(tela, cor, rect, border_radius=4)

        if eh_cabeca:
            pygame.draw.line(tela, cor, (seg_x, seg_y + 4), (seg_x - 6, seg_y - 4), 2)
            pygame.draw.line(tela, cor, (seg_x, seg_y + 16), (seg_x - 6, seg_y + 24), 2)
            pygame.draw.line(tela, cor, (seg_x + TAMANHO_BLOCO, seg_y + 4), (seg_x + TAMANHO_BLOCO + 6, seg_y - 4), 2)
            pygame.draw.line(tela, cor, (seg_x + TAMANHO_BLOCO, seg_y + 16), (seg_x + TAMANHO_BLOCO + 6, seg_y + 24), 2)

            pygame.draw.circle(tela, COR_ARANHA_OLHO, (seg_x + 6, seg_y + 7), 2)
            pygame.draw.circle(tela, COR_ARANHA_OLHO, (seg_x + 14, seg_y + 7), 2)


def desenhar_inseto(tela, inseto_x, inseto_y):
    
    pygame.draw.rect(tela, COR_INSETO, (inseto_x + 7, inseto_y + 5, 8, 12))
    pygame.draw.rect(tela, COR_INSETO_ASA, (inseto_x, inseto_y + 4, 7, 7))
    pygame.draw.rect(tela, COR_INSETO_ASA, (inseto_x + 15, inseto_y + 4, 7, 7))
    pygame.draw.rect(tela, COR_INSETO, (inseto_x + 5, inseto_y + 17, 3, 3))
    pygame.draw.rect(tela, COR_INSETO, (inseto_x + 15, inseto_y + 17, 3, 3))


def desenhar_hud(tela, fonte, pontos, recorde, tempo_decorrido_ms):
    
    segundos = calcular_tempo_decorrido(tempo_decorrido_ms)
    texto_tempo_str = formatar_tempo(segundos)

    texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    texto_recorde = fonte.render(f"Recorde: {recorde}", True, CINZA)
    texto_tempo = fonte.render(f"Tempo: {texto_tempo_str}", True, BRANCO)

    tela.blit(texto_pontos, (10, 10))
    tela.blit(texto_recorde, (10, 40))
    tela.blit(texto_tempo, (LARGURA_TELA - texto_tempo.get_width() - 10, 10))


def desenhar_fim_de_jogo(tela, fonte, fonte_grande, pontos, recorde, novo_recorde, tempo_decorrido_ms):
    
    overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    overlay.set_alpha(200)
    overlay.fill(PRETO)
    tela.blit(overlay, (0, 0))

    segundos = calcular_tempo_decorrido(tempo_decorrido_ms)
    tempo_str = formatar_tempo(segundos)

    titulo = fonte_grande.render("A ARANHA CAIU NA PROPRIA TEIA!", True, (255, 80, 80))
    tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, ALTURA_TELA // 2 - 90))

    texto_pontos = fonte.render(f"Pontuacao final: {pontos}", True, BRANCO)
    tela.blit(texto_pontos, (LARGURA_TELA // 2 - texto_pontos.get_width() // 2, ALTURA_TELA // 2 - 25))

    texto_tempo = fonte.render(f"Tempo de sobrevivencia: {tempo_str}", True, BRANCO)
    tela.blit(texto_tempo, (LARGURA_TELA // 2 - texto_tempo.get_width() // 2, ALTURA_TELA // 2 + 5))

    if novo_recorde:
        texto_recorde = fonte.render("NOVO RECORDE!", True, (255, 215, 0))
    else:
        texto_recorde = fonte.render(f"Recorde: {recorde}", True, CINZA)
    tela.blit(texto_recorde, (LARGURA_TELA // 2 - texto_recorde.get_width() // 2, ALTURA_TELA // 2 + 40))

    texto_saida = fonte.render("Pressione ESC para sair", True, CINZA)
    tela.blit(texto_saida, (LARGURA_TELA // 2 - texto_saida.get_width() // 2, ALTURA_TELA // 2 + 85))


def executar_jogo():
    tela, relogio = inicializar()
    fonte = pygame.font.Font(None, 30)
    fonte_grande = pygame.font.Font(None, 46)

    fundo_cache = _construir_fundo_gradiente()
    teia_cache = _construir_teia(pontos_brilho_seed=42)

    
    cabeca_x = (LARGURA_TELA // 2) - (LARGURA_TELA // 2) % TAMANHO_BLOCO
    cabeca_y = (ALTURA_TELA // 2) - (ALTURA_TELA // 2) % TAMANHO_BLOCO
    corpo = [
        (cabeca_x, cabeca_y),
        (cabeca_x - TAMANHO_BLOCO, cabeca_y),
        (cabeca_x - 2 * TAMANHO_BLOCO, cabeca_y),
    ]
    direcao = "DIREITA"

    inseto_x, inseto_y = gerar_posicao_inseto(corpo)

    pontos = 0
    recorde = carregar_recorde(CAMINHO_RECORDE)
    novo_recorde = False

 
    tempo_decorrido_ms = 0
    jogo_acabou = False

    
    intervalo_movimento_ms = 130
    acumulador_movimento_ms = 0

    while True:
        delta_ms = relogio.tick(FPS)

        direcao = processar_eventos(direcao)

        if not jogo_acabou:
            tempo_decorrido_ms += delta_ms

            acumulador_movimento_ms += delta_ms
            if acumulador_movimento_ms >= intervalo_movimento_ms:
                acumulador_movimento_ms = 0

                nova_cabeca = atualizar_posicao(corpo[0][0], corpo[0][1], direcao)

                comeu = (nova_cabeca == (inseto_x, inseto_y))
                if comeu:
                    pontos = calcular_pontos(pontos, 1)

                corpo = mover_corpo(corpo, nova_cabeca, comeu)

                if comeu:
                    inseto_x, inseto_y = gerar_posicao_inseto(corpo)

                if colidiu_com_proprio_corpo(nova_cabeca, corpo):
                    jogo_acabou = True

            if jogo_acabou:
                if pontos > recorde:
                    recorde = pontos
                    novo_recorde = True
                    salvar_recorde(CAMINHO_RECORDE, recorde)

        desenhar_cenario_teia(tela, fundo_cache, teia_cache)
        desenhar_inseto(tela, inseto_x, inseto_y)
        desenhar_aranha(tela, corpo, direcao)
        desenhar_hud(tela, fonte, pontos, recorde, tempo_decorrido_ms)

        if jogo_acabou:
            desenhar_fim_de_jogo(tela, fonte, fonte_grande, pontos, recorde, novo_recorde, tempo_decorrido_ms)

        pygame.display.flip()
