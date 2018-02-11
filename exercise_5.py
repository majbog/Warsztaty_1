from random import randint

allowed_die = [3, 4, 6, 8, 10, 1, 20, 100]
find_die=0
find_modifier=0
how_to_proceed = input("Co robimy?")
code = list(how_to_proceed)
find_die = code.index("d")
if "-"  in code:
    find_modifier = code.index("-")
elif "+" in code:
    find_modifier = code.index("+")
else:
    modifier = 0
modifier= code[find_modifier+1:]
modifier="" .join(modifier)
modifier=int(modifier)
die = code[find_die+1:find_modifier]
die = "" .join(die)
die = int(die)
how_many = code[:find_die]
if how_many == []:
    how_many = 1
else:
    how_many = "" .join(how_many)
    how_many = int(how_many)
while True:
    if die not in allowed_die:
        print("Something's wrong with your die")
        break
    else:
        count = 0
        final_result = 0
        result = 0
        while not(how_many == count):
            result += randint(1, die)
            count += 1
        if "-" in code:
            final_result = result - modifier
            print("Wynik: {}" .format(final_result))
            break
        else:
            final_result = result + modifier
            print ("Wynik: {}" .format(final_result))
            break




