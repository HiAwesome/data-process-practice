# coding=utf-8
import pprint

openfile = open('../../data/chp5/en-final-table9.txt', 'r')
country_line = total_line = False
previous_line = ''
countries = []
totals = []

double_lined_countries = [
    'Bolivia (Plurinational \n',
    'Democratic People\xe2\x80\x99s \n',
    'Democratic Republic \n',
    'Lao People\xe2\x80\x99s Democratic \n',
    'Micronesia (Federated \n',
    'Saint Vincent and \n',
    'The former Yugoslav \n',
    'United Republic \n',
    'Venezuela (Bolivarian \n',
]


def turn_on_off(a_line, status, start, prev_line, end='\n'):
    # 根据某一行开始和结束的字符，来决定状态表示是 开 或者 关。
    if a_line.startswith(start):
        status = True
    elif status:
        if a_line == end and prev_line != 'and areas':
            status = False
    return status


def clean(a_line):
    # 数据清洗：清洗掉特殊字符
    a_line = a_line.strip('\n').strip()
    a_line = a_line.replace('\xe2\x80\x93', '-')
    a_line = a_line.replace('\xe2\x80\x99', '\'')
    return a_line


for line in openfile:
    if country_line:
        if previous_line in double_lined_countries:
            line = ' '.join([clean(previous_line), clean(line)])
        countries.append(clean(line))

    elif total_line:
        if len(line.replace('\n', '').strip()) > 0:
            totals.append(clean(line))

    country_line = turn_on_off(line, country_line, 'and areas', previous_line)
    total_line = turn_on_off(line, total_line, 'total', previous_line)

    previous_line = line

data = dict(zip(countries, totals))
pprint.pprint(data)
