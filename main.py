
from csv_reader import (
    charger_csv,
    CsvException,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException,
    PrixInvalideException
)


if __name__ == "__main__":

    try:
        articles = charger_csv("articles.csv")

        print("Import réussi !")
        print("Liste des articles :")

        for article in articles:
            print(article)

    except FichierIntrouvableException as e:
        print("Erreur fichier :", e)

    except LigneInvalideException as e:
        print("Erreur ligne :", e)

    except PrixNegatifException as e:
        print("Erreur prix :", e)

    except PrixInvalideException as e:
        print("Erreur format du prix :", e)

    except CsvException as e:
        print("Erreur CSV :", e)
