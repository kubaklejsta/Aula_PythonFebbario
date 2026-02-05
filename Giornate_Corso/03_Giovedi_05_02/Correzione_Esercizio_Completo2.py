#Es 1

import random

# 1) Chiedi un intero positivo n (se <= 0 continua a chiedere)
n = int(input("Inserisci un numero intero positivo n: "))

while n <= 0:
    print("Errore: devi inserire un numero maggiore di 0.")
    n = int(input("Inserisci un numero intero positivo n: "))

# 2) Genera una lista di n numeri casuali tra 1 e n (incluso)
lista = []
for i in range(n):
    numero_casuale = random.randint(1, n)
    lista.append(numero_casuale)

print("\nLista generata:", lista)

# 3) Somma dei numeri pari nella lista
somma_pari = 0
for num in lista:
    if num % 2 == 0:
        somma_pari = somma_pari + num

print("\nSomma dei numeri pari:", somma_pari)

# 4) Stampa tutti i numeri dispari nella lista
print("\nNumeri dispari nella lista:")
for num in lista:
    if num % 2 != 0:
        print(num)

# 5) Funzione per controllare se un numero è primo
def is_primo(x):
    if x < 2:
        return False

    # controllo divisori da 2 a x-1
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

# 6) Stampa tutti i numeri primi nella lista
print("\nNumeri primi nella lista:")
for num in lista:
    if is_primo(num):
        print(num)

# 7) Somma di tutti i numeri nella lista e controllo se è primo
somma_totale = 0
for num in lista:
    somma_totale = somma_totale + num

print("\nSomma totale della lista:", somma_totale)

if is_primo(somma_totale):
    print("La somma totale è un numero primo!")
else:
    print("La somma totale NON è un numero primo.")


