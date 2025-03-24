from pathlib import Path

try:
    arquivo = open("meu_arquivo.txt", "r")
except FileNotFoundError as exc:
    print("Arquivo não encontrado")
    print(exc)


ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo_diretorio_2", "r")
except IsADirectoryError as exc:
    print("É um diretório")
    print(exc)
except IOError:
    print(f"Erro de I/O {exc}")
except Exception as exc:
    print(f"Algum erro ocorreu ao tentar abrir o arquivo: {exc}")