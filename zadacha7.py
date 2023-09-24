
print("1-прямоугольник, 2-треугольник, 3-круг")
s = input("Выберите фигуру: ")

match s:
    
    case '1':
        print("Длины сторон прямоугольника:")
        a = int(input("a = "))
        b = int(input("b = "))
        s = a*b
        print (s)
        
    case '2':
        print("введите высоту и основание треугольника:")
        h = int(input("h = "))
        b = int(input("b = "))
        s  = (b*h)/2
        print (s)
    
    case '3':
        r = int(input("Радиус круга r = "))
        print((3.14 * r ** 2))
        print (r)
    case _:
        print("а таких мы площадь не ищем")