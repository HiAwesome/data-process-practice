# coding=utf-8
import json
import pprint

import pymysql.cursors

# 通过 JSON 读取配置文件
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
