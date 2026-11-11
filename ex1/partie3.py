
from contextlib import ExitStack

paths = ["a.txt", "b.txt", "c.txt"]

with ExitStack() as stack:

    files = []

    # Ouvrir les fichiers
    for p in paths:
        f = stack.enter_context(open(p, "w"))
        files.append(f)

    # Écrire dans chaque fichier
    for f in files:
        f.write("test\n")

print("Tous les fichiers sont fermés")
