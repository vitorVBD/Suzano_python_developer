import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

os.mkdir(ROOT_PATH / 'novo_diretorio') # Cria uma nova pasta

arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "renomeado.txt") # Renomeia um arquivo

os.remove(ROOT_PATH / "renomeado.txt") # Remove um arquivo

shutil.move(ROOT_PATH / "novo_diretorio", ROOT_PATH / "novo_diretorio_2") # Move um arquivo