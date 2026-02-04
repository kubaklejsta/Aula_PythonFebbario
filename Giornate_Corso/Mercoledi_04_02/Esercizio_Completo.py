#ES 1 if

numero = int(input("Inserisci un numero: "))

if numero % 2 == 0:
    print("Pari")
else:
    print("Dispari")


#es 2 range e while

ripeti = "si"
n = int(input("Inserisci un numero positivo: "))

while ripeti == "si":

    for i in range(n, -1, -1):
        print(i)
    ripeti = input("Vuoi ripetere? (si/no): ")
  
#es 3 for 

numeri = [1, 2, 3, 4, 5]

for n in numeri:
    print(n * n)

# es 4

numeri = []

scelta = "si"
while scelta == "si":
    valore = int(input("Inserisci un numero: "))
    numeri.append(valore)
    scelta = input("Vuoi inserire un altro numero? (si/no): ")

if len(numeri) == 0:
    print("Lista vuota")
else:
    massimo = numeri[0]

    for n in numeri:
        if n > massimo:
            massimo = n

    conteggio = 0
    i = 0
    while i < len(numeri):
        conteggio = conteggio + 1
        i = i + 1

    print("Numero massimo:", massimo)
    print("Numero di elementi:", conteggio)

