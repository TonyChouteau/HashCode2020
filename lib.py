



# ---------------------------------------------------------------------------------------------------------------------
# Classe système
# ---------------------------------------------------------------------------------------------------------------------

class System:

    def __init__( self, max_days = 0 ):
        """
        Constructeur

        :param max_days: Nombre maximum de jour pour tout traiter.
        """

        self.libraries = []
        self.max       = max_days

    def signed_libraries( self ):
        return len([ library for library in self.libraries if len(library.scanned_books) > 0 ])


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

        # Liste des livres qui ont été signés
        self.scanned_books = []

    def add_book( self, book ):
        """
        Ajoute un livre dans la bibliothèque

        :param book: Instance de Book à ajouter
        """

        position = len( self.books )

        for i in range( len(self.books) ):
            if book.score >= self.books[i].score:
                position = i
                break

        self.books.insert( position, book )

    def scanned_books( self ):
        """
        :return: Le nombre des livres ayant eu le temps
        """

    def __str__( self ):
        """
        Affichage de la bibliothèque courante

        :return: chaine de caractère contenant les attributs de l'objet courant
        """

        return f"Bibliothèque<id: {self.id}, time: {self.time}, scannable_books_per_day: {self.scannable_books_per_day}, books: {self.books} >"



# ---------------------------------------------------------------------------------------------------------------------
# Test
# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    library = Library()
    library.add_book( Book( 1, 20 ) )
    library.add_book( Book( 2, 21 ) )
    library.add_book( Book( 3, 22 ) )
    library.add_book( Book( 4, 19 ) )

    for book in library.books:
        print( book )