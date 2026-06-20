from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    mover_corpo,
    colidiu_com_proprio_corpo,
    calcular_tempo_decorrido,
    formatar_tempo,
)


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_mover_corpo_sem_crescer_mantem_tamanho():
    """Quando a aranha nao come, o corpo anda mas mantem o mesmo tamanho."""
    corpo = [(40, 40), (20, 40), (0, 40)]
    novo_corpo = mover_corpo(corpo, (60, 40), cresceu=False)
    assert novo_corpo == [(60, 40), (40, 40), (20, 40)]
    assert len(novo_corpo) == len(corpo)


def test_mover_corpo_ao_comer_cresce_um_segmento():
    """Quando a aranha come um inseto, o corpo cresce em um segmento (a bunda aumenta)."""
    corpo = [(40, 40), (20, 40), (0, 40)]
    novo_corpo = mover_corpo(corpo, (60, 40), cresceu=True)
    assert len(novo_corpo) == len(corpo) + 1
    assert novo_corpo[0] == (60, 40)
    assert novo_corpo[-1] == corpo[-1]


def test_colidiu_com_proprio_corpo_detecta_colisao():
    """Deve detectar quando a cabeca ocupa a mesma posicao de um segmento do corpo."""
    corpo = [(40, 40), (20, 40), (0, 40)]
    assert colidiu_com_proprio_corpo((20, 40), corpo) is True


def test_colidiu_com_proprio_corpo_sem_colisao():
    """Nao deve detectar colisao quando a cabeca esta em posicao livre."""
    corpo = [(40, 40), (20, 40), (0, 40)]
    assert colidiu_com_proprio_corpo((60, 40), corpo) is False


def test_calcular_tempo_decorrido_converte_ms_para_segundos():
    """Deve converter milissegundos decorridos em segundos inteiros (cronometro)."""
    assert calcular_tempo_decorrido(15000) == 15


def test_calcular_tempo_decorrido_arredonda_para_baixo():
    """Milissegundos incompletos nao devem contar como um segundo cheio."""
    assert calcular_tempo_decorrido(15999) == 15


def test_calcular_tempo_decorrido_cresce_sem_limite():
    """O cronometro deve continuar contando, sem nenhum teto/limite."""
    assert calcular_tempo_decorrido(120000) == 120


def test_formatar_tempo_abaixo_de_um_minuto():
    """Deve formatar segundos abaixo de 60 no padrao MM:SS."""
    assert formatar_tempo(45) == "00:45"


def test_formatar_tempo_acima_de_um_minuto():
    """Deve formatar corretamente quando ha minutos e segundos."""
    assert formatar_tempo(125) == "02:05"