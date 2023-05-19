# Задача 32: Определить индексы элементов массива(списка), значения которых принадлежат заданному диапазону(т.е. не меньше заданного минимума и не больше заданного максимума)

# Input:
# 1, 3, 7, 10, 5, 8
# 4
# 8
# Output:
# 2(7), 4(5), 5(8)

arr = [1, 3, 7, 10, 5, 8]
min_val = int(input('Минимальное значение: '))
max_val = int(input('Максимальное значение: '))
indexes = []
for i in range(len(arr)):
    if arr[i] >= min_val and arr[i] <= max_val:
        indexes.append(i)

print(f'индексы элементов в массиве: {indexes}')

# решение через генератор
result = [i for i in range(len(arr)) if arr[i] >= min_val and arr[i] <= max_val]
print(result)

# эталонное решение
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input('Минимальное значение: '))
# max_number = int(input('Максимальное значение: '))
# for i in range(len(list_1)):
#   if min_number <= list_1[i] <= max_number:
#     print(f'индексы элементов в массиве: {i}')

