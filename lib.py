

# ---------------------------------------------------------------------------------------------------------------------
# Classe des livres
# ---------------------------------------------------------------------------------------------------------------------

class Book:

    def __init__( self, score = 0 ):
        """
        Constructeur

        :param score: Score du livre (entier, 0 si non indiqué)
        """
        self.score = score


# ---------------------------------------------------------------------------------------------------------------------
# Classe des bibliothèques
# ---------------------------------------------------------------------------------------------------------------------

class Library:

    def __init__( self, time = 0, scannable_books_per_day = 0 ):
        """
        Constructeur

        :param time: Nombre de jours nécessaire à l'enregistrement de la bibliothèque
        :param scannable_books_per_day: Nombre de livres que la bibliothèque peut
        """

        self.books = []
        self.time  = time
        self.scannable_books_per_day = scannable_books_per_day