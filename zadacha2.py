a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if (a > b and a < c) or (a > c and a < b):
        print(a)
elif (b > a and b < c) or (b > c and b < a):
        print(b)
elif (c > a and c < b) or (c > b and c < a):
        print(c)
elif a == b or a == c or b == c:
        print('error')