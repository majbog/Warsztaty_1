import random

machine = [i for i in range(0,50)]
random.shuffle(machine)
lotto_result = machine[:6]

while True:
    try:
        users_guess=[]
        winner =[]
        count = 1
        while (count < 7):
            i = int(input("{}. Podaj liczbę: " .format(count)))
            while ((i not in range (0, 50)) or (i in users_guess)):
                print ("Wygląda na to, że iczba jest niepoprawna")
                i = int(input("{}. Podaj liczbę: ".format(count)))
            users_guess.append(i)
            count += 1
        print("Wynik losowania: {}" .format(lotto_result))
        print("Twój strzał: {}" .format(users_guess))
        for a in lotto_result:
            if a in users_guess:
                winner.append(a)
        print ("Trafiłeś {} razy" .format(len(winner)))
        break
    except ValueError:
        print ("oops")




print("Do następnego!")
