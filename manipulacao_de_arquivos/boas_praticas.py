from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / 'arquivo.txt', 'r') as file:
        print(file.read())
except IOError as exc:
    print(f'Erro ao abrir o arquivo: {exc}')

try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as file:
        file.write("Aprendendo a manipular arquivos utilizando Python")
except IOError as exc:
    print(f'Erro ao abrir o arquivo: {exc}')
except UnicodeDecodeError as exc:
    print(f'Erro ao decodificar o arquivo: {exc}')