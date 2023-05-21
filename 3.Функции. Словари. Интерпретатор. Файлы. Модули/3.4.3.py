import os
with open('C:/Users/79825/Desktop/text.txt', 'r+', encoding='utf-8') as file, open('C:/Users/79825/Desktop/OUT.txt','w') as out:
    a = []
    s = file.read().split()
    a = [i.split(';') for i in s]
    math = 0
    phys = 0
    rus = 0
    for i in a:
        d = ((int(i[1]) + int(i[2]) + int(i[3]))/(len(a[0]) - 1))
        math += int(i[1])
        phys += int(i[2])
        rus += int(i[3])
        out.write(str(d) + '\n')
    out.write(str(math / len(a)) + ' ')
    out.write(str(phys / len(a)) + ' ')
    out.write(str(rus / len(a)))
