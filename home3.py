print("Камень, ножницы, бумага")
print("Интсрукция:")
print("r - камень", "s - ножницы", "p - бумага")
start = input("Если вы готовы введите что угодно: ")

import random
draw = 0
comp = 0
hum = 0
list = ["r", "s", "p"]
"r" > "s"
"s" > "p"
"p" > "r"

print("Для завершения введите Y")
while True:
    computer = random.choice(list)
    human = str(input("Выберите r/s/p: "))
    if human.lower() == "y":
        break
    else:
        if human == "r":
            if human.lower() == "y":
                break
            else:
                print(computer)
                if str(computer) > str(human):
                    comp = comp + 1
                    print("Победа компьютера")
                elif str(computer) == str(human):
                    draw = draw + 1
                    print("Ничья")
                elif str(computer) < str(human):
                    print("Победа человека")
                    hum = hum + 1
                if comp > hum:
                    print(comp, hum, "В пользу компьютера")
                elif comp == hum:
                    print(comp, hum, "Равный счёт")
                else:
                    print(hum, comp, "В пользу человека")


        elif human == "s":
            if human.lower() == "y":
                break
            else:
                print(computer)
                if str(computer) > str(human):
                    comp = comp + 1
                    print("Победа компьютера")
                elif str(computer) == str(human):
                    draw = draw + 1
                    print("Ничья")
                elif str(computer) < str(human):
                    print("Победа человека")
                    hum = hum + 1
                if comp > hum:
                    print(comp, hum, "В пользу компьютера")
                elif comp == hum:
                    print(comp, hum, "Равный счёт")
                else:
                    print(hum, comp, "В пользу человека")



        elif human == "p":
            if human.lower() == "y":
                break
            else:
                print(computer)
                if str(computer) > str(human):
                    comp = comp + 1
                    print("Победа компьютера")
                elif str(computer) == str(human):
                    draw = draw + 1
                    print("Ничья")
                elif str(computer) < str(human):
                    print("Победа человека")
                    hum = hum + 1
                if comp > hum:
                    print(comp, hum, "В пользу компьютера")
                elif comp == hum:
                    print(comp, hum, "Равный счёт")
                else:
                    print(hum, comp, "В пользу человека")
        else:
            print("Выберете одно из данного")
            continue
            

print("Конечный счёт:", "Человек -", hum, "Компьютер -", comp)
print("Ничьих -", draw)