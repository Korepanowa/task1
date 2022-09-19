#Перейдём к созданию словарей:
dictionary1 = {}
dictionary2 = {
    "d1":"Алгебра",
    "d2":"Геометрия",
    "d3":"Литература",
    "d4":"Физика",
    "d5":"Химия",
}
print(dictionary2)

#Изменим элемент d3:
dictionary2['d3'] = 'География'
print(dictionary2)

#Создадим ещё один словарь:
dictionary3 = {'i1':'История','i2':'Биология','i3':'Обществознание'}
dictionary2.update(dictionary3)
print(dictionary2)

#Удалим элемент со значением "Биология":
del dictionary2['i2']
print(dictionary2)

#Проверим, есть ли в словаре необходимый элемент:
print('d4' in dictionary2)
print('i5' in dictionary2)

#Получим элемент:
print(dictionary2['i3'])

#Удалим все элементы в словаре:
dictionary2.clear()
print(dictionary2)