# es 1

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def distanza_da_origine(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


# programma principale
p = Punto(3, 4)
print(p.distanza_da_origine())  # distanza iniziale

p.muovi(1, -2)
print(p.distanza_da_origine())  # distanza dopo lo spostamento

# es 2

class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        return "Il libro '" + self.titolo + "' è stato scritto da " + self.autore + " e ha " + str(self.pagine) + " pagine."


# programma principale
libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
print(libro1.descrizione())


