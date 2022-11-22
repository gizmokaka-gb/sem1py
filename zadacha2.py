# 2. Напишите программу для проверки истинности утверждения
  # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))
z = int(input('Введите координату Z: '))

left = not (x or y or z)
right = not x and not y and not z
result = left == right

for x in range(0, 1):
    for y in range(0, 1):
        for z in range(0, 1):
            if result == True:
                print('Утверждение истинно')
            else:
                print('Утверждение ложно')
