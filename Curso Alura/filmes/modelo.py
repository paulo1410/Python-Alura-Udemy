class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome
    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @nome.setter
    def nome (self, nome):
        self._nome = nome

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes} Likes"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes"

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporada} - {self._likes} Likes"

# class Playlist(list):  transformar Playlist em lista recorrendo a herança
#     def __init__(self, nome, lista_programas):
#         super().__init__(lista_programas)
#         self.nome = nome
class Playlist:
    def __init__(self, nome, lista_programas):
        self.nome = nome
        self._lista_programas = lista_programas

    def __getitem__(self, item):
        return self._lista_programas[item]

    def __len__(self):
        return len(self._lista_programas)


filme1 = Filme('vingadores - gerra inifinita', 2018, 160)
filme2 = Filme('todo mundo em panico', 199, 100)
filme1.dar_like()
filme1.dar_like()
filme1.dar_like()
filme2.dar_like()

serie1 = Serie ("Breaking Bad", 2005, 5)
serie2 = Serie ("Demolidor", 2016, 2)
serie1.dar_like()
serie1.dar_like()
serie1.dar_like()
serie1.dar_like()
serie1.dar_like()
serie2.dar_like()
serie2.dar_like()



filmes_e_series = [filme1, filme2, serie1, serie2]
fds = Playlist("Fim de Semana", filmes_e_series)
print(f"Tamanho do Playlist: {len(fds)}")
for lista_programas in fds:
    print (lista_programas)
#   detalhes = programa.duracao if hasattr(programa,"duracao") else programa.temporada


