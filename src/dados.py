def salvar_recorde(caminho_arquivo, pontuacao):
    
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

        if conteudo == "":
            return 0

        return int(conteudo)

    except (FileNotFoundError, ValueError):
        return 0