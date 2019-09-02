#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import random

# locPath='G:\\车管家项目资料\\'
locPath='E:\\考勤\\杭走临安\\'
host = '888'
# port = '3306'
user = '888'
pwd = '888'
dbs = '888'

startDate='2019-08-01'
endDate='2019-09-01'


def getCheckInfo(userName,companyName):
    db = pymysql.connect(host=host, user=user,password=pwd,database=dbs,charset='utf8')
    cursor = db.cursor()
    getNumSql = '''SELECT COUNT(*), b.xmbm FROM attendance_day_report a LEFT JOIN project b ON a.xmbm = b.xmbm WHERE a.user_name = \''''+userName+'''\' AND a.DATE >= \''''+startDate+'''\' AND a.DATE < \''''+endDate+'''\'  AND a.iswork = 1 AND b.xmmc LIKE '%'''+companyName+'''%' ORDER BY a.receive_time '''
    print(getNumSql)
    cursor.execute(getNumSql)
    results = cursor.fetchall()
    db.close()
    if results != None:
        return {"sum":results[0][0],"companyCode":results[0][1]}
    else:
        return None

def updateWork(userName,companyCode,limit):
    db = pymysql.connect(host=host, user=user, password=pwd, database=dbs, charset='utf8')
    cursor = db.cursor()
    updateWorkSql = '''UPDATE attendance_day_report a SET a.iswork = 0 WHERE a.user_name = \''''+userName+'''\' AND a.date >= \''''+startDate+'''\' AND a.date < \''''+endDate+'''\'  AND a.iswork = 1 AND a.xmbm =\''''+companyCode+'''\' ORDER BY a.date LIMIT '''+str(limit)
    print(updateWorkSql)
    try:
        cursor.execute(updateWorkSql)
        db.commit()
        print('修改完成：'+userName+','+str(limit))
    except Exception as e:
        print(e)
        print('修改错误：'+userName)
        db.rollback()
    db.close()

def updateWorkAll(userName, companyCode):
    db = pymysql.connect(host=host, user=user, password=pwd, database=dbs, charset='utf8')
    cursor = db.cursor()
    updateAll='''UPDATE attendance_day_report t SET t.iswork = 0 WHERE t.user_name IN (\''''+userName+'''\') AND t.date >= \''''+startDate+'''\' AND t.date < \''''+endDate+'''\' AND t.xmbm =\''''+companyCode+'''\'  AND t.iswork = 1'''
    print(updateAll)
    try:
        cursor.execute(updateAll)
        db.commit()
        print('修改完成：' + userName)
    except Exception as e:
        print(e)
        print('修改错误：' + userName)
        db.rollback()
    db.close()

def checkWork(path):
    for line in open(path, "r",encoding='utf-8'):
        line=line.rstrip('\n')
        if ''==line or None==line:
            continue
        txtData=line.split(',')
        checkWorkDate=getCheckInfo(txtData[1],txtData[0])
        dateNum=31
        if '低于20%' == txtData[2]:
            count=random.randint(2,5)
            if checkWorkDate['sum']-count>0 and checkWorkDate['sum']>5:
                checkNum = checkWorkDate['sum']-count
                updateWork(txtData[1],checkWorkDate['companyCode'],checkNum)
        elif '考勤率为0' == txtData[2]:
            updateWorkAll(txtData[1],checkWorkDate['companyCode'])
        elif '改成90%' == txtData[2]:
            updateWork(txtData[1], checkWorkDate['companyCode'],checkWorkDate['sum']-28)
        else:
            print('错误：'+txtData[2])



if __name__ == '__main__':
    path = locPath + '123.txt'
    checkWork(path)
    print('完成')