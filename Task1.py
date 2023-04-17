# # На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной
# # Выведите минимальное количество монет, которые нужно перевернуть

import random
coins = [random.randint(0, 1) for _ in range(9)]
print(coins)

count_zero = 0
count_one = 0
for coin in coins:
    if coin == 0:
        count_zero += 1
    else:
        count_one += 1
if count_zero > count_one:
    print('Перевернуть единички')
else:
    print('Перевернуть нолики')
