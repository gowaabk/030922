""" Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y). """


number = int(input('Введите номер плоскости  N -> '))


if (number == 1):
    print('Точка в плоскости ', number,
          ' имеет возможные координаты X > 0 и Y > 0')
elif (number == 2):
    print('Точка в плоскости ', number,
          ' имеет возможные координаты X < 0 и Y > 0')
elif (number == 3):
    print('Точка в плоскости ', number,
          ' имеет возможные координаты X < 0 и Y < 0')
else:
    print('Точка в плоскости ', number,
          ' имеет возможные координаты X > 0 и Y < 0')