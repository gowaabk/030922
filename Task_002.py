""" Напишите программу для. проверки истинности утверждения
 ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. """


def find_truth(x, y, z):
    res_left = not (x or y or z)
    res_right = not (x and y and z)
    if res_left == res_right:
        result = True
    else:
        result = False
    return result


m = [0, 0, 0,
     0, 0, 1,
     0, 1, 0,
     0, 1, 1,
     1, 0, 0,
     1, 0, 1,
     1, 1, 0,
     1, 1, 1]
for i in range(0, 24, 3):
    x = m[i]
    y = m[i+1]
    z = m[i+2]
    print(x, y, z, ' --> ', find_truth(x, y, z))
