#es 1 

ripeti = "si"

while ripeti == "si":
    numero = int(input("Inserisci un numero: "))

    for i in range(numero, -1, -1):
        print(i)

    ripeti = input("Vuoi ripetere? (si/no): ")



# es 2

numeri_primi = []
conteggio = 0

while conteggio < 5:
    numero = int(input("Inserisci un numero: "))

    if numero < 2:
        print("Il numero non è primo")
    else:
        primo = True

        for i in range(2, numero):
            if numero % i == 0:
                primo = False

        if primo:
            print("Il numero è primo")
            numeri_primi.append(numero)
            conteggio = conteggio + 1
        else:
            print("Il numero non è primo")

print("Hai inserito 5 numeri primi:", numeri_primi)

