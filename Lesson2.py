# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

A = int(input("Введите число: "))
current = 1
previous = 0
i = 2

while current < A:
    temp = current
    current = previous + current
    previous = temp
    i = i + 1
if current == A:
    print(i)
else:
    print(-1)



