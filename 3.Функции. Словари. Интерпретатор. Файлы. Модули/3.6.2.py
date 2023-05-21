import requests


with open('C:/Users/79825/Downloads/dataset_3378_3.txt', 'r+', encoding='utf-8') as file, open('C:/Users/79825/Desktop/OUT.txt','w') as out:
    #  читаю url из файла, обрезаю пробелы
    url = file.read().strip()
    # отправляю запрос по полученному url
    r = requests.get(url)
    while True:
        # пока новый файл не начнется с "We"
        if not r.text.startswith('We'):
            # перебираем файлы
            r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)
            print(r.text)# смотрим, пока перебор файлов происходит
            continue
        out.write(r.text)
        break
