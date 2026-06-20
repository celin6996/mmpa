"""Ponto de entrada do jogo Spider Grow.

A logica do jogo vive em src/jogo.py para manter o codigo organizado
em modulos pequenos (config, funcoes, dados, sprites, jogo) e para
permitir que as regras puras sejam testadas em tests/test_logica.py.
"""
from src.jogo import executar_jogo

if __name__ == "__main__":
    executar_jogo()
