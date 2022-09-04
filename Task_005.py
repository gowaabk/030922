"""     Напишите программу, которая принимает на вход координаты двух точек
    и находит расстояние между ними в 2D пространстве.

    Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
 """
import math
point_x1 = int(input('Input X1 ->'))
point_y1 = int(input('Input Y1 ->'))

point_x2 = int(input('Input X2 ->'))
point_y2 = int(input('Input Y2 ->'))

distanse = math.sqrt((point_x1 - point_x2)**2 + (point_y1 - point_y2)**2)
print(round(distanse, 2))
