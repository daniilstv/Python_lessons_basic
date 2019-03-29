# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    a = str(number)
    b = a.find(".")
    c = b + ndigits + 1
    
    x = int(a[0:b])
    y = int(a[b+1:c])
    z = y
    
    if int(a[c]) >= 5:
        z += 1

    if len(str(y)) < len(str(z)):
        x += 1
        z = str(z)
        z = z[1:]

    d = str(x) + "." + str(z)
    return(float(d))

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    a = str(ticket_number)[0:3]
    b = str(ticket_number)[3:6]
    return(sum([int(x) for x in str(a)]) == sum([int(x) for x in str(b)]))  


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

