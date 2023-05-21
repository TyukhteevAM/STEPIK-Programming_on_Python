import requests


with open('C:/Users/79825/Downloads/dataset_3378_2.txt', 'r+', encoding='utf-8') as file, open('C:/Users/79825/Desktop/OUT.txt','w') as out:
    #  читаю url из файла, обрезаю пробелы
    url = file.read().strip()
    # отправляю запрос по полученному url
    r = requests.get(url)
    d = r.text
    # читаю количество строк в полученном файле
    out.write(str(d.count('\n')))