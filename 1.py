#Списки
#Создадим список школьных предметов
subjects = ['biology','chemistry','physics']

print(subjects)
#Для преобразования в список:

s = list()
print(s)

#Возьмём другой тип данных и преобразуем его в список 
scroll = ('geometry','geography')
s = list(scroll)
print(s)

#Получим конкретный элемент списка через его позицию
print(subjects[-1])
print(list(scroll[1]))#Просто интересно было, что получится)
print(s[-1])
print(s[0])

#Выведем всё содержимое списков в отдельном списке
scrolls = [scroll,subjects]
print(scrolls)

#Добавим ещё элементов в содержисое списков
scrolls = [scroll,'algebra','history',subjects]
print(scrolls)

#Изменим элемент в определённой позиции
scrolls[2] = 'astronomy'
print(scrolls) 

#Выведем несколько элемеентов в определённом диапазоне:
print(scrolls[0:3])

#Выведем нечётные элементы:
print(scrolls[::2])

#Инвертируем список
print(scrolls[::-1])

#Добавим ещё один элемент в конец списка:
scrolls.append('literature')
print(scrolls)

#Объединим несколько списков в один
subjects.extend(s)
print(subjects)

subjects += scrolls 
print(subjects)

#Используем функцию insert() и добавим элемент на определённую позицию
subjects.insert(2, 'art')
print(subjects)

#Удалим элемент на позиции 1 - химию
del subjects[1]
print(subjects)

#Рассмотрим другие способы удаления:
subjects.pop(4)
print(subjects)

subjects.remove('art')
print(subjects)


#Узнаем индекс определённого элемента
print(subjects.index('physics'))

#Проверим, есть ли в данном списке элемент с определённым значением
print('art' in subjects) #Ранее удалённый элемент не может быть в списке

#Просмотрим, сколько раз содержится значение в списке
print(subjects.count('physics'))
print(subjects.count('geometry'))


subjects.append('geometry')
print(subjects.count('geometry'))


#Изменим поряд элементов в списке, отсортируем список:
s.sort()
print(s)

s_scroll = sorted(scroll)
print(s_scroll)

#Узнаем длину списка со списками)
print(len(scrolls))

#Создадим список и скопируем его:
scroll1 = ['Свиток','Список','Перечень']
scroll2 = scroll1.copy()
print(scroll2)

#Данное копирование позволяет изменять оригинал не теряя данные:
scroll1[1]='Лист'
print(scroll1)
print(scroll2)