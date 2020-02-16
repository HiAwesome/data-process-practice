# coding=utf-8
import json
import pprint

import pymysql.cursors

"""
    通过 JSON 读取配置文件，需要在顶级目录的 conf/mysql_config.json 进行配置
    方法参考：https://blog.csdn.net/matrix_google/article/details/76671797
"""
with open('../../conf/mysql_config.json', 'rb') as confFile:
    confStr = confFile.read()
conf = json.JSONDecoder().decode(confStr)

connection = pymysql.connect(host=conf['host'],
                             user=conf['user'],
                             password=conf['password'],
                             db=conf['db'],
                             charset=conf['charset'],
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM person where id = 7"
        cursor.execute(sql)
        result = cursor.fetchone()
        pprint.pprint(result)
finally:
    connection.close()
