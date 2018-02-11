

def let_me_guess():
    min = 0
    max = 1000
    answer_if_yes = ""
    need_some_help = ""
    count = 1
    while True:
        guess = int((max - min) / 2 + min)
        print('Zgaduję: {}'.format(guess))
        answer_if_yes = input("Zgadłem? (tak/nie)")
        if answer_if_yes in ("tak"):
            print("Super! Trafiłem za {} razem. Dzięki za wspólną zabawę" .format(count))
            break
        else:
            count += 1
            need_some_help = input("Za dużo? Za mało?")
            if need_some_help in ("Za dużo"):
                max = guess
            elif need_some_help in ("Za mało"):
                min = guess
            else:
                print("Wybacz, nie zrozumiałem")
    print("To wszystko na dzisiaj!")






print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę  w max. 10 próbach")
print(let_me_guess())
