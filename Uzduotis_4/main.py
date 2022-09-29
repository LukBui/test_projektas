# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.

class Movie:
    '''Klase parodanti filmo pavadinima, direktoriu ir biudzeta'''
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget
    def was_expensive(budget):
        '''Patikrina ar filmo biudzetas daugiau nei 100 mln.'''
        if budget > 100000000:
            return True

movie = Movie('Titanikas', 'Vinas Dyzelis', 15000)