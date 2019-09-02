#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

host = '*******'
port = '3306'
user = '*******'
pwd = '*******'
db = '*******'
getNumSql = '''SELECT COUNT(*), b.xmbm FROM attendance_day_report a LEFT JOIN project b ON a.xmbm = b.xmbm WHERE a.user_name = '{0}' AND a.DATE >= '2019-08-01' AND a.DATE < '2019-09-01'  AND a.iswork = 1 AND b.xmmc LIKE '%{1}%' ORDER BY a.receive_time '''
updateSql = '''UPDATE attendance_day_report a SET a.iswork = 0 WHERE a.user_name = '金云泉' AND a.date >= '2019-06-01' AND a.date < '2019-07-01'  AND a.iswork = 1 AND a.xmbm ='' ORDER BY a.date LIMIT 3 '''
updateAll='''UPDATE attendance_day_report t SET t.iswork = 0 WHERE t.user_name IN ('何培德') AND t.date >= '2019-06-01' AND t.date < '2019-07-01' AND t.iswork = 1'''

def checkWork():
    db = pymysql.connect(host, user, pwd,'123')
    cursor = db.cursor()
    cursor.execute(getNumSql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]


if __name__ == '__main__':
    checkWork()