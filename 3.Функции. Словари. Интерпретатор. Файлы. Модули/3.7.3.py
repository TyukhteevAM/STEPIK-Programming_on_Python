"""создаем множество-словарь через генератор, все слова приводим к нижнему регистру"""
list_of_worlds = set([input().lower() for i in range(int(input()))])
"""создаем список-список для проверки через генератор, все слова приводим к нижнему регистру """
list_of_check = [input().lower().split() for k in range(int(input()))]
"""из списка для проверки создаем множество"""
a = set(sum(list_of_check, []))
"""вычитаем из множества для проверки множество-словарь"""
c = a - list_of_worlds
"""печатаем все отсутствующие в словаре списки, каждое слово на новой строке"""
print(*c, sep='\n')