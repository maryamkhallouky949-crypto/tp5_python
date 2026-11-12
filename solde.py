
class SoldeInsuffisantException(Exception):
    def __init__(self, message):
        super().__init__(message)


class CompteBancaire:
    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde

    def deposer(self, montant):
        if montant <= 0:
            print("Montant invalide.")
        else:
            self.solde += montant

    def retirer(self, montant):
        if montant <= 0:
            print("Montant invalide.")
        elif montant > self.solde:
            raise SoldeInsuffisantException(
                "Solde insuffisant pour ce retrait."
            )
        else:
            self.solde -= montant

    def afficher(self):
        print(f"Compte: {self.nom}, Solde: {self.solde}€")


if __name__ == "__main__":
    try:
        compte = CompteBancaire("maryam", 200)
        compte.afficher()

        compte.retirer(230)

        compte.afficher()

    except SoldeInsuffisantException as e:
        print("Erreur:", e)
