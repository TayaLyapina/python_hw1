# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Введите трехзначное число: '))
first_digit = n//100
second_digit = (n//10)%10
third_digit = n%10
print(f'Сумма цифр трехзначного числа: {first_digit+second_digit+third_digit}')

