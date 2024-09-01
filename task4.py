# Задание №6
# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

gregorian = 158
big_leap_year = 400
small_leap_year = 4
no_leap_year = 100

year = int(input("Введите год - "))

if year < gregorian:
    if not year % small_leap_year:
        result = "Год является високосным по Юлианскому календарю."
    else:
        result = "Год не високосный по Юлианскому календарю."
elif year % no_leap_year and not year % small_leap_year or year % big_leap_year == 0:
    result = "Год является високосным по Григорианскому календарю."
else:
    result = "Год не високосный по Григорианскому календарю."

print(result)