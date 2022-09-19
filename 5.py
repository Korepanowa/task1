#В качестве предметной области было выбрано школьное рассписание:

subjects = 'Алгебра','Геометрия','Химия','Физика','География','История','Литература','ИЗО'

days = 'Понедельник','Вторник','Среда','Четверг','Пятница'

asking_for_lessons = {
    days[0]:[subjects[0],subjects[1],subjects[2],subjects[4],subjects[7]],
    days[1]:[subjects[2],subjects[1],subjects[5],subjects[6]],
    days[2]:[subjects[4],subjects[0],subjects[1],subjects[5],subjects[3]],
    days[3]:[subjects[0],subjects[1],subjects[1]],
    days[4]:[subjects[0],subjects[0],subjects[3],subjects[3]]
}
print(asking_for_lessons)