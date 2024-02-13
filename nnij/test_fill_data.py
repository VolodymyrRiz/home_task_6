from datetime import datetime
import faker
import random
from random import randint, choice
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 5
NUMBER_MARKS = 150

def generate_fake_data(number_groups, number_students, number_teachers, number_subjects, number_marks):
    fake_groups = []  # тут зберігатимемо групи
    fake_students = []  # тут зберігатимемо сстудентів
    fake_teachers = []  # тут зберігатимемо вчителів
    fake_subjects = []  # тут зберігатимемо дисципліни
    fake_marks = []  # тут зберігатимемо оцінки
    '''Візьмемо три групи з faker і помістимо їх у потрібну змінну'''
    fake_data = faker.Faker()

    # Створимо набір груп у кількості number_groups
    for er in range(number_groups):
        fake_groups.append(str(er))

    # Згенеруємо тепер number_students кількість студентів'''
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Та number_teachers набір вчителів
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())
        
     # Згенеруємо тепер number_subjects кількість дисциплін'''
    for _ in range(number_subjects):
        fake_subjects.append(fake_data.job())

    # Та number_marks набір оцінок
        
    for _ in range(number_marks):
        mrk = random.randint(60, 100)
        fake_marks.append(mrk)

    return fake_groups, fake_students, fake_teachers, fake_subjects, fake_marks

def prepare_data(groups_nnij, students_nnij, teachers_nnij, subjects_nnij, marks_nnij):
    for_groups = []
    # готуємо список кортежів назв груп
    for name_ in groups_nnij:
        for_groups.append((name_))

    for_students = []  # для таблиці students_nnij
    for student in students_nnij:
       for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_teachers = [] # для таблиці teachers_nnij
    for teacher in teachers_nnij:
        for_teachers.append((teacher, randint(1, NUMBER_GROUPS)))
        
    for_subjects = [] # для таблиці subjects_nnij     
    for subject_ in subjects_nnij:
        for_subjects.append((subject_, randint(1, NUMBER_TEACHERS)))
        
    for_marks = [] # для таблиці marks_nnij   
    ns = 1
    ns1 = 1
    nd = 1
    nd1 = 1
    for mark in marks_nnij:
        
        if ns == NUMBER_SUBJECTS + 1:
            ns = 1
            ns1 = ns1 + 1
        if nd == NUMBER_SUBJECTS + 1:
            nd = 1
            nd1 = 1
        for_marks.append((ns1, nd1, mark))
        ns += 1
        nd += 1
        nd1 += 1
    
    return  for_groups, for_students, for_teachers, for_subjects, for_marks

groups_nnij, students_nnij, teachers_nnij, subjects_nnij, marks_nnij = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_SUBJECTS, NUMBER_MARKS))
print(groups_nnij)
print(students_nnij)
print(teachers_nnij)
print(subjects_nnij)
print(marks_nnij)

