#Код Саліги Артема, код не ідеальний і має багато помилок, доробити до кінця не маю змоги так як закінчився час




x = int(input ("Введіть кількість рядків і колонок від 1 до 3---"))
if x > 3:
    print ("Це число більше за 3")
else:
    from random import randint

    n, m = x, x
    a = [[] for i in range(n)]
    for i in range(n):
        for j in range(m):
            a[i].append(randint(1, 10))
    for i in range(len(a)):
        print(a[i])

        row0 = a[0]
        row0sum = sum(a[0])

        if 3 > x > 1:
            row0 = a[0]
            row0sum = sum(a[0])
            row1 = a[1]
            row1sum = sum(a[1])
        if 4 > x > 2:
            row0 = a[0]
            row0sum = sum(a[0])
            row1 = a[1]
            row1sum = sum(a[1])
            row2 = a[2]
            row2sum = sum(a[2])



if 3 > x > 1:
    b = [(row0sum), (row1sum)]
elif 4 > x > 2:
    b = [(row0sum), (row1sum), (row2sum)]

b.sort()

print ("Відсортований масив")
if (row0sum) < (row1sum) < (row2sum):
    print (a[0])
    print (a[1])
    print (a[2])
elif (row0sum) > (row1sum) > (row2sum):
    print(a[2])
    print(a[1])
    print(a[0])
elif (row0sum) < (row1sum) > (row2sum) > (row0sum):
    print(a[0])
    print(a[2])
    print(a[1])
elif (row0sum) < (row1sum) > (row2sum) < (row0sum):
    print(a[2])
    print(a[0])
    print(a[1])

















