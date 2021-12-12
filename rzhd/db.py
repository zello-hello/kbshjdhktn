import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2.extras

import config


def connect_to_db():
    try:
        con = psycopg2.connect(
            database=config.DATABASE,
            user=config.USER,
            password=config.PASSWORD,
            host=config.HOST,
            port=config.PORT
        )
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return con
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def connection_select(sql):
    con = connect_to_db()
    with con:
        with con.cursor() as cur:
            cur.execute(sql)
            row = cur.fetchall()
            return row


def connection_insert_update(sql):
    con = connect_to_db()
    with con:
        with con.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(sql)


def push_request(number, year, theme, function, test):
    connection_insert_update(f'insert into requests (Номер, Год, Тема_открытого_запроса,'
                             f'Функциональный_заказчик, test) '
                             f'values (\'{number}\', \'{year}\', \'{theme}\', '
                             f'\'{function}\', \'{test}\')'
                             )


def push_project(number, name, decsription, company, fio, telephone, function, status):
    connection_insert_update(f'insert into projects (Номер, Название_проекта, Описание_проекта, Компания, ФИО, '
                             f'телефон, Текущий_статус)'
                             f'values (\'{number}\', \'{name}\', \'{decsription}\', \'{company}\', '
                             f'\'{fio}\', \'{telephone}\', \'{function}\', \'{status}\')'
                             )


"""
Projects

Номер; Название проекта; Описание проекта; Компания; Ф.И.О.; телефон; Текущий статус

Номер, Название_проекта, Описание_проекта, Компания, ФИО, телефон, Текущий_статус
"""



"""
Requests

№ п/п;Год;Тема открытого запроса;Функциональный заказчик;;

Номер,Год,Тема_открытого_запроса,Функциональный_заказчик,test,


"""

