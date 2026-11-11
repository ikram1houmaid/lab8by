
import csv
from datetime import datetime


class BatchProcessor:

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.fichier_csv = None
        self.journal = None

    def __enter__(self):
        try:
            # Ouvrir le fichier CSV en lecture
            self.fichier_csv = open(
                self.csv_file, "r", encoding="utf-8", newline=""
            )

            # Ouvrir le fichier journal en ajout
            self.journal = open(
                "journal.log", "a", encoding="utf-8"
            )

            self.journal.write(
                f"[{datetime.now()}] Début du traitement\n"
            )
            self.journal.flush()

            print("Fichiers ouverts avec succès.")

            return self

        except (OSError, UnicodeError) as e:

            # Fermer les fichiers déjà ouverts en cas d'erreur
            if self.fichier_csv is not None:
                self.fichier_csv.close()

            if self.journal is not None:
                self.journal.close()

            raise OSError(f"Erreur d'ouverture : {e}") from e

    def traiter(self):

        try:
            lecteur = csv.reader(self.fichier_csv)

            for ligne in lecteur:

                if not ligne:
                    continue

                operation = ligne[0]

                print(f"Traitement de l'opération : {operation}")

                # Traitement simulé
                resultat = operation.upper()

                print(f"Résultat : {resultat}")

                self.journal.write(
                    f"[{datetime.now()}] "
                    f"Opération : {operation} -> {resultat}\n"
                )

                self.journal.flush()

        except (OSError, csv.Error, UnicodeError) as e:
            raise RuntimeError(
                f"Erreur pendant le traitement : {e}"
            ) from e

    def __exit__(self, exc_type, exc_value, traceback):

        # Enregistrer la fin du traitement
        try:
            if self.journal is not None:

                if exc_type:
                    self.journal.write(
                        f"[{datetime.now()}] "
                        f"Traitement interrompu : {exc_value}\n"
                    )
                else:
                    self.journal.write(
                        f"[{datetime.now()}] "
                        "Fin du traitement avec succès\n"
                    )

                self.journal.flush()

        except OSError as e:
            print(f"Erreur d'écriture dans le journal : {e}")

        finally:

            # Fermer les deux fichiers
            if self.fichier_csv is not None:
                self.fichier_csv.close()

            if self.journal is not None:
                self.journal.close()

            print("Tous les fichiers sont fermés.")

        return False


# Programme principal
try:

    with BatchProcessor("operations.csv") as processor:

        processor.traiter()

except (OSError, RuntimeError) as e:

    print(f"Erreur : {e}")
