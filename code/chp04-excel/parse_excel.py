# coding=utf-8
"""
    这是用来分析童工和童婚数据的脚本
    本脚本中用到的 Excel 文件可以在以下链接中获取:
        http://www.unicef.org/sowc2014/numbers/
"""

import pprint

import xlrd

book = xlrd.open_workbook('../../data/chp4/SOWC 2014 Stat Tables_Table 9.xlsx')

sheet = book.sheet_by_name('Table 9 ')

data = {}

# 从第 14 行开始，因为这是国家数据的起点
for i in xrange(14, sheet.nrows):
    row = sheet.row_values(i)

    country = row[1]
    data[country] = {
        'child_labor': {
            'total': [row[4], row[5]],
            'male': [row[6], row[7]],
            'female': [row[8], row[9]],
        },
        'child_marriage': {
            'married_by_15': [row[10], row[11]],
            'married_by_18': [row[12], row[13]],
        }
    }

    # 最后一个国家是津巴布韦
    if country == 'Zimbabwe':
        break

pprint.pprint(data)
