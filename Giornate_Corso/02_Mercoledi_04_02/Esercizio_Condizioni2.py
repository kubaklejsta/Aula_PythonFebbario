#es 1

eta = int(input("Inserisci la tua età: "))

match eta:
    case _:
        if eta < 18:
            print("Mi dispiace, non puoi vedere questo film")
        else:
            print("Puoi vedere questo film")


#es 2

num1 = int(input("Inserisci primo numero: "))
num2 = int(input("Inserisci secondo numero: "))
operazione = input("Inserisci operazione (+ - * /): ")

match operazione:
    case "+":
        risultato = num1 + num2
        print(risultato)

    case "-":
        risultato = num1 - num2
        print(risultato)

    case "*":
        risultato = num1 * num2
        print(risultato)

    case "/":
        if num2 == 0:
            print("Errore: Divisione per zero")
        else:
            risultato = num1 / num2
            print(risultato)

    case _:
        print("Operazione non valida")
