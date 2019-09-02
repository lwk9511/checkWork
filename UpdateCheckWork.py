#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql


host = '*******'
port='3306'
user = '*******'
pwd = '*******'
db = '*******'

def checkWork():
    --修改考勤数据为不合格
    SELECT
    COUNT(*), b.xmbm
    FROM
    attendance_day_report
    a
    LEFT
    JOIN
    project
    b
    ON
    a.xmbm = b.xmbm
    WHERE
    a.user_name = '朱潮洪'
    AND
    a.DATE >= '2019-08-01'
    AND
    a.DATE < '2019-09-01'
    AND
    a.iswork = 1
    AND
    b.xmmc
    LIKE
    '%临安青山湖-大园新城二期一标段%'
    ORDER
    BY
    a.receive_time;

    UPDATE
    attendance_day_report
    a
    SET
    a.iswork = 0
    WHERE
    a.user_name = '金云泉'
    AND
    a.date >= '2019-06-01'
    AND
    a.date < '2019-07-01'
    AND
    a.iswork = 1
    AND
    a.xmbm = ''
    ORDER
    BY
    a.date
    LIMIT
    3;

    --修改考勤数据为0
    SELECT * FROM
    `attendance_day_report`
    WHERE
    user_name
    IN('朱潮洪', '陈飞阳')
    AND
    DATE >= '2019-03-01'
    AND
    DATE < '2019-04-01'
    AND
    iswork = 1
    ORDER
    BY
    receive_time
    DESC;

    UPDATE
    `attendance_day_report`
    t
    SET
    t.iswork = 0
    WHERE
    t.user_name
    IN('何培德')
    AND
    t.date >= '2019-06-01'
    AND
    t.date < '2019-07-01'
    AND
    t.iswork = 1;