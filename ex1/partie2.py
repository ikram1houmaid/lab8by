
from pathlib import Path
from contextlib import contextmanager

@contextmanager
def temp_file():

    path = Path("temp.txt")
    f = path.open("w")

    print("Fichier ouvert")

    try:
        yield f

    finally:
        f.close()
        path.unlink()
        print("Fichier fermé et supprimé")


# Utilisation
with temp_file() as f:
    f.write("Autre test\n")
    f.write("Test avec contextmanager\n")

print("Fin du programme")
