#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

number = int(input('Введите номер билета: '))
first_digit = number // 100000
second_digit = (number // 10000) % 10
third_digit = (number // 1000) % 10
fourth_digit = (number // 100) % 10
fifth_digit = (number // 10) % 10
sixth_digit = number % 10
if first_digit + second_digit + third_digit == fourth_digit + fifth_digit + sixth_digit:
    print('YES')
else:
    print('NO')