def calcular_pontos(pontos_atual, pontos_ganhos):
  
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    
    return vida_atual - dano


def jogador_perdeu(vidas):
   
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
  
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):

    return retangulo_1.colliderect(retangulo_2)


def mover_corpo(corpo, nova_cabeca, cresceu):
    
    novo_corpo = [nova_cabeca] + list(corpo)
    if not cresceu:
        novo_corpo.pop()
    return novo_corpo


def colidiu_com_proprio_corpo(cabeca, corpo):
  
    return cabeca in corpo[1:]


def calcular_tempo_decorrido(tempo_decorrido_ms):

    return tempo_decorrido_ms // 1000


def formatar_tempo(segundos_totais):
    
    minutos = segundos_totais // 60
    segundos = segundos_totais % 60
    return f"{minutos:02d}:{segundos:02d}"