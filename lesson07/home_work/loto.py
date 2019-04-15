#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random

barrel_set = random.sample(range(1, 91), 90)

def card(): # генератор карточки
    card_set = random.sample(range(1, 91), 15)
    
    a = []
    for i in range(5):
        a.append(card_set.pop())    
    a = sorted(a)
    for i in range(4):
        a.insert(random.randrange(0, 8, 1), ". ")

    b = []
    for i in range(5):
        b.append(card_set.pop())    
    b = sorted(b)
    for i in range(4):
        b.insert(random.randrange(0, 8, 1), ". ")
#    print(*b)

    c = []
    for i in range(5):
        c.append(card_set.pop())    
    c = sorted(c)
    for i in range(4):
        c.insert(random.randrange(0, 8, 1), ". ")
#    print(*c)
    return a+b+c
    

print("       Игра Лото\n")



# Печать карточек
print("------ Ваша карточка -----")
my_card = card()
print(*my_card[0:9])
print(*my_card[9:18])
print(*my_card[18:27])
print("-"*27)
print('\n')

print("-- Карточка компьютера ---")
npc_card = card()
print(*npc_card[0:9])
print(*npc_card[9:18])
print(*npc_card[18:27])
print("-"*27)


# через функции
my_score = 0
npc_score = 0

def lose():
    print("Вы проиграли!")



def game_set():
    my_score = 0
    npc_score = 0
    open_barrel = barrel_set.pop()
    print("Открыт бочонок:",open_barrel, " осталось в мешке ", len(barrel_set))
    answer = input("Зачеркнуть цифру? выйти? (y/n/q)")

    if answer == "y":  

        for i in range(len(my_card)):
            if my_card[i] == open_barrel:
                print("Зачеркнута цифра", my_card[i])
                my_card[i] = "-"
                my_score += 1
                check_win()
                game_set()
                return my_score
#            else:
#                lose()
#                break
                
    if answer == "n":
        
        
        pass
    if answer == "q":
        print("До свидания")

def print_cards():     
    print("------ Ваша карточка -----")
#    my_card = card()
    print(*my_card[0:9])
    print(*my_card[9:18])
    print(*my_card[18:27])
    print("-"*27)
    print('\n')

    print("-- Карточка компьютера ---")
#    npc_card = card()
    print(*npc_card[0:9])
    print(*npc_card[9:18])
    print(*npc_card[18:27])
    print("-"*27)                


def check_win():
    if my_score == 15:
        print("Вы выиграли!")
    elif npc_score == 15 and my_score == 15:
        print("Ничья")
    else:
        lose()



