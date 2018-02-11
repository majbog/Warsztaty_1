from random import randint

x = randint(0, 100)

while True:
    try:
        a = (input('Zgadnij liczbę (0-100): '))
        a1 = int(a)
        if a1 == x:
            print ("Zgadłeś!")
            break
        elif not a1 in range (0,100):
            print ("W skali od 0 do 100, misiu!")
        elif a1 < x:
            print ("Za mało!")
        else:
            print ("Za dużo")
    except TypeError:
        print ("Liiczbę...")
    except ValueError:
        print ("Liiczbę, ok?")

print("Dziękujemy za wspólną zabawę")


