import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Id", "Nome"])
        escritor.writerow(["1", "Vitor"])
        escritor.writerow(["2", "João"])
        escritor.writerow(["3", "Maria"])
except IOError as exc:
    print(f"Algum erro aconteceu: {exc}")


try:
    with open(ROOT_PATH / "usuarios.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)
except IOError as exc:
    print(f"Algum erro aconteceu: {exc}")