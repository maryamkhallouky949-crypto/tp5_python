
class ReservationException(Exception):
    def __init__(self, message):
        super().__init__(message)


class CapaciteDepasseeException(ReservationException):
    pass


class NombreInvalideException(ReservationException):
    pass


class NomClientInvalideException(ReservationException):
    pass


class Evenement:
    def __init__(self, nom, capacite):
        if capacite <= 0:
            raise NombreInvalideException(
                "La capacité doit être positive."
            )

        self.nom = nom
        self.capacite = capacite
        self.places_reservees = 0

    def reserver(self, nom_client, nb_places):

        if not nom_client.strip():
            raise NomClientInvalideException(
                "Nom du client requis."
            )

        if nb_places <= 0:
            raise NombreInvalideException(
                "Nombre de places invalide."
            )

        if self.places_reservees + nb_places > self.capacite:
            raise CapaciteDepasseeException(
                "Capacité dépassée."
            )

        self.places_reservees += nb_places

        print(
            f"Réservation confirmée pour {nom_client} "
            f"({nb_places} places)."
        )

    def afficher(self):
        print(
            f"Événement: {self.nom} — "
            f"{self.places_reservees}/{self.capacite} "
            f"places réservées"
        )


if __name__ == "__main__":

    event = Evenement("Concert", 6)

    try:
        event.reserver("", 3)

    except ReservationException as e:
        print("Erreur:", e)

    event.afficher()
