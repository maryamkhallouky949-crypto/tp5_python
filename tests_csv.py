
import unittest
import tempfile
import os

from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException,
    PrixInvalideException
)


class TestCSV(unittest.TestCase):

    def creer_fichier(self, contenu):
        fichier = tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="",
            suffix=".csv",
            delete=False
        )

        fichier.write(contenu)
        fichier.close()

        self.addCleanup(os.unlink, fichier.name)

        return fichier.name

    def test_csv_valide(self):
        chemin = self.creer_fichier(
            "id;nom;prix\n"
            "1;Clavier;150\n"
            "2;Souris;80\n"
            "3;Ecran;1200\n"
        )

        articles = charger_csv(chemin)

        self.assertEqual(len(articles), 3)
        self.assertEqual(articles[0]["nom"], "Clavier")
        self.assertEqual(articles[0]["prix"], 150.0)

    def test_fichier_absent(self):
        with self.assertRaises(FichierIntrouvableException):
            charger_csv("fichier_inexistant.csv")

    def test_ligne_invalide(self):
        chemin = self.creer_fichier(
            "id;nom;prix\n"
            "1;Clavier\n"
        )

        with self.assertRaises(LigneInvalideException):
            charger_csv(chemin)

    def test_prix_texte(self):
        chemin = self.creer_fichier(
            "id;nom;prix\n"
            "1;Clavier;abc\n"
        )

        with self.assertRaises(PrixInvalideException):
            charger_csv(chemin)

    def test_prix_negatif(self):
        chemin = self.creer_fichier(
            "id;nom;prix\n"
            "1;Clavier;-50\n"
        )

        with self.assertRaises(PrixNegatifException):
            charger_csv(chemin)


if __name__ == "__main__":
    unittest.main()
