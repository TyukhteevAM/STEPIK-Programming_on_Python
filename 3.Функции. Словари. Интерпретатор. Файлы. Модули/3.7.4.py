a = [0, 0] #водим начальные координаты
b = [input().split() for i in range(int(input()))] #задаем направление движения в двумерный массив)
for i in b: #шагаем по координатам в цикле
    if i[0] == 'север':
        a[1] += int(i[1])
    elif i[0] == 'запад':
        a[0] -= int(i[1])
    elif i[0] == 'юг':
        a[1] -= int(i[1])
    elif i[0] == 'восток':
        a[0] += int(i[1])
print(*a) #выводим конечные координаты