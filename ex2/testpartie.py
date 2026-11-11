
from datetime import datetime
from contextlib import ExitStack

class ConnectionManager:

    def __init__(self, service_name):
        self.service_name = service_name

    def __enter__(self):
        print(f"Connexion à {self.service_name} établie.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Déconnexion de {self.service_name}.")

        if exc_type:
            print(f"Erreur : {exc_value}")

        return False


services = ["Serveur A", "Serveur B", "Serveur C"]

with ExitStack() as stack:

    connections = []

    for service in services:
        conn = stack.enter_context(ConnectionManager(service))
        connections.append(conn)

    for conn in connections:
        print(f"Travail effectué sur {conn.service_name}")

print("Toutes les connexions sont fermées.")
