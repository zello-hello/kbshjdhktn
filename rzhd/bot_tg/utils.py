from aiogram.dispatcher.filters.state import StatesGroup, State


'''

Проект
['id',
 'Номер',
 'Название_проекта',
 'Описание_проекта',
 'Компания',
 'ФИО',
 'телефон',
 'Функциональный_заказчик',
 'Текущий_статус']


Запрос
['id',
 'Номер',
 'Год',
 'Тема_открытого_запроса',
 'Функциональный_заказчик',
 'test']


'''


class RegRequest(StatesGroup):
    year_state = State()

    request_theme_state = State()

    functional_requester_state = State()


class RegProject(StatesGroup):
    name_state = State()

    description_state = State()

    company_state = State()

    fio_state = State()

    telephone_number = State()

    functional_requester_state = State()

    current_status = State()


