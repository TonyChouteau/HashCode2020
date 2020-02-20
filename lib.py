

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

    def __str__( self ):
        """
        Affichage du livre courant

        :return: chaine de caractère contenant les attributs de l'objet courant
        """

        return f"Livre<id: {self.id}, score: {self.score}>"



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

    def __str__( self ):
        """
        Affichage de la bibliothèque courante

        :return: chaine de caractère contenant les attributs de l'objet courant
        """

        return f"Bibliothèque<id: {self.id}, time: {self.time}, scannable_books_per_day: {self.scannable_books_per_day}, books: {self.books} >"