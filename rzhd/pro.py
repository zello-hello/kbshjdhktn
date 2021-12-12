import db


def get_clean_file(file_name):
    a = []
    f = open(file_name, 'r')
    for i in f.readlines():
        i = i.strip().strip('\ufeff').replace('\n', ' ')
        if i.count(';;') > 0:
            for j in range(i.count(';;')):
                i = i.replace(';;', ';')
        a.append(i.split(';'))
    return a


def write_file(file_name, array):
    f = open(file_name, 'w')
    for i in array:
        a = ';'.join(i)
        print(a)
        f.write(a)
        f.write('\n')


def make_dict(array):
    cur_ar_dict = []
    first = array[0]
    for i_array in array[1:]:
        cur_dict = {}
        for i, j in zip(i_array, first):
            cur_dict[j] = i
        cur_ar_dict.append(cur_dict)
    return cur_ar_dict


project = get_clean_file('Реестр проектов.csv')

# write_file('project.csv', project.csv)
# g = get_clean_file('project2.csv')
# print(*g, sep='\n')
k = open('ans','w')
# print(*make_dict(project), sep='\n', file=k)


requests = get_clean_file("Перечень открытых запросов.csv")

print(requests)

# for i in requests[1:]:
#     print(i)
#     db.push_request(*i[:5])
print('ok')
# print(*make_dict(requests), sep='\n', file=k)

print(db.connection_select(f'select r.id as "номер", r.Тема_открытого_запроса, p.id, p."Название_проекта", r."Функциональный_заказчик", p."Функциональный_заказчик" from requests as r join projects as p '
                           f'on r."Функциональный_заказчик" = p."Функциональный_заказчик" or not position(' ' || r."Функциональный_заказчик" || ' ' in p."Функциональный_заказчик") = 0;'
                           ''))






"""
array = [['1','2','3','3','3','3','1']]
cur_dict = {}
for i_array in range(len(array)):
    for i_words in array[i_array]:
        cur_dict[i_words] = array[i_array].count(i_words)
print(cur_dict)
"""

"""
Номер;Название проекта;Описание проекта;Компания;Ф.И.О.;телефон;Текущий статус;
"""