def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def mover_corpo(corpo, nova_cabeca, cresceu):
    """Atualiza a lista de segmentos do corpo da aranha.

    Insere a nova posição da cabeça no início da lista. Se a aranha não
    comeu (cresceu=False), remove o último segmento para manter o
    tamanho; se comeu (cresceu=True), mantém o segmento extra e a
    aranha cresce em um bloco (cresce "a bunda", ou seja, a parte
    final do corpo).
    """
    novo_corpo = [nova_cabeca] + list(corpo)
    if not cresceu:
        novo_corpo.pop()
    return novo_corpo


def colidiu_com_proprio_corpo(cabeca, corpo):
    """Verifica se a cabeça da aranha colidiu com algum segmento do corpo."""
    return cabeca in corpo[1:]


def calcular_tempo_decorrido(tempo_decorrido_ms):
    """Retorna o tempo decorrido em segundos inteiros (cronômetro, sem limite)."""
    return tempo_decorrido_ms // 1000


def formatar_tempo(segundos_totais):
    """Formata uma quantidade de segundos no padrão MM:SS."""
    minutos = segundos_totais // 60
    segundos = segundos_totais % 60
    return f"{minutos:02d}:{segundos:02d}"