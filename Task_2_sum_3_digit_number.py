# Задача 2: Найдите сумму цифр трехзначного числа.

#Способ 1:
# a = int (input("Введите трёхзначное число: "))
# if 99<a<999:
#     print(int(a/100) + int(a%100/10) + int(a%10))
# else:
#     print('Введите трёхзначное число!!!')

#Способ 2:
# a = int (input("Введите трёхзначное число: "))
# if 99 < a < 999:
#     summa = 0
#     while a > 0:
#         b = a%10
#         summa = summa + b
#         a = a//10
#     print(summa)
# else:
#     print('Введите трёхзначное число!!!')

# Способ 3:
# a = input('Введите трёхзначное число: ')
# if len(a) == 3:
#     print(int(a[0]) + int(a[1]) + int(a[2]))
# else:
#     print('Введите трёхзначное число!!!')

#Способ 4:
a = input('Введите трёхзначное число: ')
if len(a) == 3:
    summa = 0
    for i in a[:]:
        summa = summa + int(i)
    print(summa)
else:
    print('Введите трёхзначное число!!!')