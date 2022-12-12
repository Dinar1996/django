# total = 0
# natural = int(input())
# for i in range(natural- 1,1,-1):
#     if (natural % i == 0):
#         total = total + i
# print(total)
#

numb = int(input("Введите целое число: "))
sum_of_dividers = 0
for i in range(numb - 1, 1, -1):
    if (numb % i == 0):
        sum_of_dividers += i
print("Сумма:", sum_of_dividers)

