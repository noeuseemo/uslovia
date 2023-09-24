a = int(input('введите коэф.а- '))
b = int(input('введите коэф.б- '))
c = int(input('введите коэф с- '))

v = (b**2) - (4*a*c)

if v<0:
    print('no result')

elif v == 0:
    x = round((-b) / (2*a), 2)
    print(f'x = {x}')

else:
    x1 = round((-b + (v)) / (2*a), 2)
    x2 = round((-b - (v)) / (2*a), 2)

if x1 == x2:
    print(f'x1 = x2 = {x1}')

else:
    print(f'x1 = {x1}\nx2 = {x2}')