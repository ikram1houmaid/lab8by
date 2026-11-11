
from contextlib import contextmanager
from pathlib import Path

@contextmanager
def temp_file():

    path = Path("temp.txt")
    print("Ouverture du fichier")

    f = path.open("w")

    try:
        yield f

    finally:
        f.close()
        print("Fermeture du fichier")

        if path.exists():
            path.unlink()
            print("Suppression du fichier")


with temp_file() as f:
    f.write("Bonjour Python\n")
