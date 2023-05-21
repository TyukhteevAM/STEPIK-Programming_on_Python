import os
with open('C:/Users/79825/Desktop/text.txt', 'r+', encoding='utf-8') as file, open('C:/Users/79825/Desktop/OUT.txt','w') as out:
    a = []
    # читаю строки, соединяю в массив
    s = file.read().split()
    # создаю двумерный массив (каждый студент со совим набором оценок)
    a = [i.split(';') for i in s]
    # завожу накопительные счетчики по каждому предмету
    math = 0
    phys = 0
    rus = 0
    for i in a:
        # считаю ср.зн по каждому значению для каждого ученика
        d = ((int(i[1]) + int(i[2]) + int(i[3]))/(len(a[0]) - 1))
        math += int(i[1])
        phys += int(i[2])
        rus += int(i[3])
        # записываю результат в файл каждый раз с новой строки
        out.write(str(d) + '\n')
    # считаю ср. арифм по каждому предмету и пишу в файсл с новой строки
    out.write(str(math / len(a)) + ' ' + str(phys / len(a)) + str(rus / len(a)))

