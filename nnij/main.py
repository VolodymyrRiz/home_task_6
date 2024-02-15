#import create_db
# import fill_data
import query_1
import query_2
import query_3
import query_4
import query_5
import query_6
import query_7
import query_8
import query_9
import query_10
import sqlite3
import os


def create():
    create_db.run()
    pass


def fill_data():
    fill_data.run()
    pass


def query(number):
    with open('query_'+ number +'.sql', 'r') as f:
        sql = f.read()  
    with sqlite3.connect('nnij_new.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()          
 

if __name__ == "__main__":
    number = ''
    #create()
    #fill_data()
    while True:
        print('Виберіть номер запиту: ')
        print('Знайти 5 студентів із найбільшим середнім балом з усіх предметів - 1 + Enter')
        print('Знайти 5 студентів із найбільшим середнім балом з усіх предметів - 2 + Enter')
        print('Знайти 5 студентів із найбільшим середнім балом з усіх предметів - 3 + Enter')
        print('Знайти 5 студентів із найбільшим середнім балом з усіх предметів - 4 + Enter')
        print('Знайти 5 студентів із найбільшим середнім балом з усіх предметів - 5 + Enter')
        print('Знайти 5 студентів із найбільшим середнім балом з усіх предметів - 6 + Enter')
        print('Знайти 5 студентів із найбільшим середнім балом з усіх предметів - 7 + Enter')
        print('Знайти 5 студентів із найбільшим середнім балом з усіх предметів - 8 + Enter')
        print('Знайти 5 студентів із найбільшим середнім балом з усіх предметів - 9 + Enter')
        print('Знайти 5 студентів із найбільшим середнім балом з усіх предметів - 10 + Enter')
        print('Припинити запити - 0 + Enter')    
        input(str(number))        
        if number == '0':
            os.abort()
        print(query(str(number)))
        continue
                