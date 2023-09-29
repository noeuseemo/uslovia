year = int(input('введите год: '))

if year % 4 == 0:
        if year % 100 != 0:
            print('год високосный')
        else:
            if year % 400 == 0:
                print('год  високосный')
            else:
                print('год не високосный')
else:
        print('год не високосный')
