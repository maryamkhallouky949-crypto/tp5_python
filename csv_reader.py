
import csv
import logging
import os

logging.basicConfig(
    filename="erreurs.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class CsvException(Exception):
    pass



class FichierIntrouvableException(CsvException):
    pass

class LigneInvalideException(CsvException):
    pass

class PrixNegatifException(CsvException):
    pass

class PrixInvalideException(CsvException):
    pass


def charger_csv(chemin):

    articles = []

    try:
        with open(chemin, "r", encoding="utf-8", newline="") as fichier:

            lecteur = csv.reader(fichier, delimiter=";")

            entete = next(lecteur, None)

            if entete != ["id", "nom", "prix"]:
                raise LigneInvalideException(
                    "En-tête CSV incorrect."
                )

            
            for numero, ligne in enumerate(lecteur, start=2):

               
                if not ligne or all(col.strip() == "" for col in ligne):
                    continue

                
                if len(ligne) != 3:
                    raise LigneInvalideException(
                        f"Ligne {numero} : trois colonnes sont attendues."
                    )

                identifiant, nom, prix = ligne

                if not identifiant.strip() or not nom.strip():
                    raise LigneInvalideException(
                        f"Ligne {numero} : identifiant ou nom manquant."
                    )

            
                try:
                    prix = float(prix)
                except ValueError:
                    raise PrixInvalideException(
                        f"Ligne {numero} : prix non numérique."
                    )

            
                if prix < 0:
                    raise PrixNegatifException(
                        f"Ligne {numero} : prix négatif."
                    )

                if prix == 0:
                    raise PrixInvalideException(
                        f"Ligne {numero} : le prix doit être supérieur à zéro."
                    )

                article = {
                    "id": identifiant,
                    "nom": nom,
                    "prix": prix
                }

                articles.append(article)

    except FileNotFoundError:
        message = f"Fichier introuvable : {chemin}"
        logging.error(message)
        raise FichierIntrouvableException(message)

    except CsvException as erreur:
        logging.error(str(erreur))
        raise

    return articles
