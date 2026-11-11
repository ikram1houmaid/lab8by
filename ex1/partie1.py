
from pathlib import Path

class TempFileWriter:

    def __enter__(self):
        self.filepath = Path("temp.txt")
        self.f = self.filepath.open("w")
        print("Fichier ouvert")
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        self.filepath.unlink()
        print("Fichier fermé et supprimé")

        return False


# Utilisation
with TempFileWriter() as f:
    f.write("Contenu temporaire\n")
    f.write("Deuxième ligne\n")

print("Fin du programme")
