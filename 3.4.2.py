import os
with open('C:/Users/79825/Desktop/text.txt', 'r+', encoding='utf-8') as file, open('C:/Users/79825/Desktop/OUT.txt','w') as out:
    maxc = 0
    s = file.read().lower().strip().split()
    s.sort()
    print(s)
    for i in s:
        counter = s.count(i)
        if counter > maxc:
            maxc = counter
            result_word = i
    out.write(result_word +' ' + str(maxc))