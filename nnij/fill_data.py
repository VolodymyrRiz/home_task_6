from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 5
NUMBER_MARKS = 150


def generate_fake_data(number_groups, number_students, number_teachers, number_subjects, number_marks) -> tuple():
    fake_groups = []  # тут зберігатимемо групи
    fake_students = []  # тут зберігатимемо сстудентів
    fake_teachers = []  # тут зберігатимемо вчителів
    fake_subjects = []  # тут зберігатимемо дисципліни
    fake_marks = []  # тут зберігатимемо оцінки
    '''Візьмемо три групи з faker і помістимо їх у потрібну змінну'''
    fake_data = faker.Faker()

    # Створимо набір груп у кількості number_groups
    for _ in range(number_groups):
        fake_groups.append(fake_data.group())

    # Згенеруємо тепер number_students кількість студентів'''
    for _ in range(number_students):
        fake_students.append(fake_data.student())

    # Та number_teachers набір вчителів
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.teacher())
        
     # Згенеруємо тепер number_subjects кількість дисциплін'''
    for _ in range(number_subjects):
        fake_subjects.append(fake_data.subject())

    # Та number_marks набір оцінок
    for _ in range(number_marks):
        fake_marks.append(fake_data.mark())

    return fake_groups, fake_students, fake_teachers, fake_subjects, fake_marks


def prepare_data(companies, employees, posts) -> tuple():
    for_companies = []
    # готуємо список кортежів назв компаній
    for company in companies:
        for_companies.append((company, ))

    for_employees = []  # для таблиці employees

    for emp in employees:
        '''
        Для записів у таблицю співробітників нам потрібно додати посаду та id компанії. Компаній у нас було за замовчуванням
        NUMBER_COMPANIES, при створенні таблиці companies для поля id ми вказували INTEGER AUTOINCREMENT - тому кожен
        запис отримуватиме послідовне число збільшене на 1, починаючи з 1. Тому компанію вибираємо випадково
        у цьому діапазоні
        '''
        for_employees.append((emp, choice(posts), randint(1, NUMBER_COMPANIES)))

    '''
   Подібні операції виконаємо й у таблиці payments виплати зарплат. Приймемо, що виплата зарплати у всіх компаніях
    виконувалася з 10 по 20 числа кожного місяця. Діапазон зарплат генеруватимемо від 1000 до 10000 у.о.
    для кожного місяця, та кожного співробітника.
    '''
    for_payments = []

    for month in range(1, 12 + 1):
        # Виконуємо цикл за місяцями'''
        payment_date = datetime(2021, month, randint(10, 20)).date()
        for emp in range(1, NUMBER_EMPLOYESS + 1):
            # Виконуємо цикл за кількістю співробітників
            for_payments.append((emp, payment_date, randint(1000, 10000)))

    return for_companies, for_employees, for_payments


def insert_data_to_db(companies, employees, payments) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('salary.db') as con:

        cur = con.cursor()

        '''Заповнюємо таблицю компаній. І створюємо скрипт для вставлення, де змінні, які вставлятимемо, відзначимо
        знаком заповнювача (?) '''

        sql_to_companies = """INSERT INTO companies(company_name)
                               VALUES (?)"""

        '''Для вставлення відразу всіх даних скористаємося методом executemany курсора. Першим параметром буде текст
        скрипта, а другим - дані (список кортежів).'''

        cur.executemany(sql_to_companies, companies)

        # Далі вставляємо дані про співробітників. Напишемо для нього скрипт і вкажемо змінні

        sql_to_employees = """INSERT INTO employees(employee, post, company_id)
                               VALUES (?, ?, ?)"""

        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(sql_to_employees, employees)

        # Останньою заповнюємо таблицю із зарплатами

        sql_to_payments = """INSERT INTO payments(employee_id, date_of, total)
                              VALUES (?, ?, ?)"""

        # Вставляємо дані про зарплати

        cur.executemany(sql_to_payments, payments)

        # Фіксуємо наші зміни в БД

        con.commit()


if __name__ == "__main__":
    companies, employees, posts = prepare_data(*generate_fake_data(NUMBER_COMPANIES, NUMBER_EMPLOYESS, NUMBER_POST))
    insert_data_to_db(companies, employees, posts)
