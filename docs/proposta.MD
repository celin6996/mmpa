# Spider Grow

## Integrantes do Grupo

* Arthur Moraes Braga Araujo
* Matheus Possemato Lopes
* Pedro Marcos
* Marcelo Artur Soares Sartori

---

## Tipo de Jogo

Spider Grow e um jogo inspirado no classico Snake (Cobrinha), desenvolvido em Python utilizando a biblioteca Pygame.

---

## Descricao Geral

O jogador controla uma aranha que se movimenta pelo mapa em busca de insetos. A cada inseto coletado, o abdomen da aranha aumenta de tamanho, tornando a movimentacao mais dificil.

O objetivo e sobreviver pelo maior tempo possivel enquanto acumula pontos e evita colisoes.

---

## Objetivo

* Coletar insetos espalhados pelo mapa.
* Aumentar a pontuacao.
* Fazer a aranha crescer.
* Evitar colisoes com as paredes e com o proprio corpo.

---

## Regras Principais

* A aranha se movimenta continuamente.
* Os insetos aparecem em posicoes aleatorias.
* Cada inseto coletado aumenta a pontuacao.
* Cada inseto coletado aumenta o tamanho da aranha.
* Colidir com uma parede encerra a partida.
* Colidir com o proprio corpo encerra a partida.

---

## Condicao de Vitoria

O jogador vence ao atingir a pontuacao maxima definida pelo grupo ou ao alcancar o tamanho limite da aranha.

---

## Condicao de Derrota

O jogo termina quando a aranha:

* Colide com uma parede;
* Colide com o proprio corpo.

---

## Elementos do Jogo

### Aranha

Personagem principal controlado pelo jogador.

### Insetos

Objetos colecionaveis que aumentam a pontuacao e fazem a aranha crescer.

### Mapa

Area onde ocorre a partida e onde aparecem os insetos.

### Sistema de Pontuacao

Registra a quantidade de insetos coletados durante a partida.

---

## Controles

| Tecla | Acao                |
| ----- | ------------------- |
| ↑     | Mover para cima     |
| ↓     | Mover para baixo    |
| ←     | Mover para esquerda |
| →     | Mover para direita  |
| ESC   | Sair do jogo        |

---

## Organizacao Inicial do Codigo

```text
SpiderGrow/
│
├── main.py
├── assets/
│   ├── images/
│   └── sounds/
│
├── src/
│   ├── aranha.py
│   ├── insetos.py
│   ├── jogo.py
│   └── config.py
│
└── docs/
    └── proposta.md
```

---

## Recursos Externos Previstos

* Imagens gratuitas para representar a aranha e os insetos.
* Tutoriais sobre Pygame para consulta.
* Icones e sprites livres para uso academico.

---

## Principais Dificuldades Esperadas

* Implementacao do crescimento da aranha.
* Deteccao de colisoes.
* Geracao aleatoria dos insetos.
* Organizacao do codigo em modulos.
* Controle da pontuacao.

---

## Escopo Minimo

A versao minima do jogo devera conter:

* Movimentacao da aranha;
* Coleta de insetos;
* Crescimento da aranha;
* Sistema de pontuacao;
* Colisao com paredes;
* Colisao com o proprio corpo;
* Tela de fim de jogo.

---

## Melhorias Futuras

Caso haja tempo disponivel, o grupo pretende adicionar:

* Tela inicial;
* Sistema de ranking;
* Sons e efeitos sonoros;
* Diferentes tipos de insetos;
* Aumento gradual da velocidade;
* Sistema de fases.
