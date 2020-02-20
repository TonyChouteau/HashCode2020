

# ---------------------------------------------------------------------------------------------------------------------
# Classe des livres
# ---------------------------------------------------------------------------------------------------------------------

class Book:

    def __init__( self, ID_book = 0, score = 0 ):
        """
        Constructeur

        :param ID_book: Identifiant du livre (entier, 0 si non indiqué)
        :param score: Score du livre (entier, 0 si non indiqué)
        """
        self.id    = ID_book
        self.score = score


# ---------------------------------------------------------------------------------------------------------------------
# Classe des bibliothèques
# ---------------------------------------------------------------------------------------------------------------------

class Library:

    def __init__( self, ID_lib = 0, time = 0, scannable_books_per_day = 0 ):
        """
        Constructeur

        :param id: Identifiant de la bibliothèque (entier, 0 si non indiqué)
        :param time: Nombre de jours nécessaire à l'enregistrement de la bibliothèque (entier, 0 si non indiqué)
        :param scannable_books_per_day: Nombre de livres que la bibliothèque peut scanner (entier, 0 si non indiqué)
        """

        self.id    = ID_lib
        self.books = []
        self.time  = time
        self.scannable_books_per_day = scannable_books_per_day