
from datetime import datetime
from contextlib import ExitStack

class ConnectionManager:

    def __init__(self, service_name):
        self.service_name = service_name

    def __enter__(self):
        print(f"[{datetime.now()}] Connexion à {self.service_name} établie.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"[{datetime.now()}] Déconnexion de {self.service_name}.")

        if exc_type:
            print(f"Erreur détectée : {exc_type.__name__} — {exc_value}")

        return False


try:

    with ExitStack() as stack:

        log = stack.enter_context(
            open("log.txt", "a", encoding="utf-8")
        )

        conn = stack.enter_context(
            ConnectionManager("Base Y")
        )

        log.write(f"[{datetime.now()}] Début du traitement\n")

        print("Traitement de la base de données...")

        # Provoquer une erreur volontaire
        raise RuntimeError("Erreur de traitement")

except RuntimeError as e:
    print(f"Exception récupérée : {e}")

print("Fin du programme.")
