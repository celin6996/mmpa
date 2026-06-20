# Spider Grow - Aranha Faminta

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Nome do integrante 1
- Nome do integrante 2
- Nome do integrante 3
- Nome do integrante 4

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

O jogo consiste em controlar uma aranha sobre um cenário de teia estilizado. A aranha se move continuamente pelo tabuleiro e cresce (ganha um novo segmento no corpo) cada vez que come um inseto. O jogador deve evitar que a aranha colida com o próprio corpo. Um cronômetro no canto da tela conta quantos segundos o jogador está sobrevivendo — ele não é um limite de tempo, é apenas um contador informativo que sobe enquanto a partida continua.

## Objetivo do jogador

Comer o maior número possível de insetos, fazendo a aranha crescer, e sobreviver o máximo de tempo possível sem deixar a cabeça da aranha colidir com o próprio corpo.

## Regras do jogo

- A aranha se move continuamente em uma direção sobre o cenário de teia, estilo "jogo da cobrinha".
- O jogador controla a direção usando as setas do teclado.
- Cada inseto comido aumenta a pontuação em 1 ponto e faz a aranha crescer um segmento (o corpo, incluindo a parte final, aumenta).
- Um cronômetro (canto superior direito) conta os segundos de sobrevivência, sem nenhum limite — ele não encerra a partida.
- O jogo só termina quando a cabeça da aranha colide com o próprio corpo.
- Se a pontuação final superar o recorde salvo, um novo recorde é gravado em `data/recorde.txt`.

## Controles

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- ESC: sair do jogo

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final do grupo e integrantes.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
