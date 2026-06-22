# Testes

Esta pasta contém testes automatizados do projeto.

## Arquivos

* `test_logica.py`: valida funções puras de lógica em `src/funcoes.py`.

## Como executar

```bash
python -m pytest
```

## Boas práticas

* Crie testes para todas as regras de pontuação, crescimento da aranha e condições de fim de jogo.
* Prefira funções pequenas, simples e testáveis no módulo `src/funcoes.py`.
* Evite dependências desnecessárias entre testes.
* Garanta que os testes sejam independentes entre si.
