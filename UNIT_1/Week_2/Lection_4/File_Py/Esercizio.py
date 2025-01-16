print("Ciao, sono ChatBot, scegli una delle figure sotto e vediamo insieme il risultato! \n")
print("1 - Quadrato")
print("2 - Cerchio")
print("3 - Rettangolo \n")

sceltaFigura = int(input(">>> "))

if sceltaFigura  == 1:
    print("Complimenti, hai scelto il Quadrato")
    lato = int(input("Inserisci il valore del lato in cm: "))
    print("Il perimetro del tuo quadrato è:", lato*4, "cm")

elif sceltaFigura == 2:
    print("Complimenti, hai scelto il Cerchio")
    raggio = float(input("Inserisci un valore: "))
    print("Il raggio del tuo cerchio è:", raggio*2*3.14)

elif sceltaFigura == 3:
    print("Complimenti, hai scelto il Rettangolo")
    base = int(input("Inserisci la base: "))
    altezza = int(input("Inserisci l'altezza: "))
    print("Il perimetro del tuo rettangolo è:", base*2 + altezza*2, "cm")

else:
    print("La scelta che hai fatto non è valida!")