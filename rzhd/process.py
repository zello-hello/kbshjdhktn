from db import *
import pandas as pd


def input_words_request(request):
    request = request.lower().split(' ')
    exception_words = ['VR', 'AR']

    for word in request:
        if len(word) <= 3 and word not in exception_words:
            request.remove(word)

    request = list(map(lambda x: x[:-2] if len(x) > 3 else x, request))
    return request


def selection_by_keywords(words):
    for word in words:
        yield pd.DataFrame(connection_select(
            f"""SELECT p.id, p."Описание_проекта", p."Название_проекта" FROM projects AS p WHERE NOT POSITION(' ' || '{word}' IN p."Описание_проекта" || p."Название_проекта") = 0;""")).values.tolist()


def rating_by_words_projects(a, name='dict1'):
    a = input_words_request(a)
    print(a)
    cur_dict = dict()

    asav = selection_by_keywords(a)
    for i in asav:
        for number in i:
            # number = number[0]
            print(number)
            if number[0] not in cur_dict:
                cur_dict[number[0]] = {"Индекс релевантности": 1, "Название проекта": number[1],
                                       "Описание проекта": number[2]}
            else:
                cur_dict[number[0]]["Индекс релевантности"] += 1

    cur_dict = dict(sorted(cur_dict.items(), key=lambda item: item[0], reverse=True))

    df = pd.DataFrame(data=cur_dict)

    df = (df.T)
    df.to_excel(name + '.xlsx', index_label='ID в базе данных')

    return name
