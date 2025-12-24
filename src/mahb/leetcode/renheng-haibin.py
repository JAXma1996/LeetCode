# -*- coding: utf-8 -*-
import urllib2
# 本次要抢的 时间是
from util import login,book_course,headers

from datetime import datetime, timedelta
import time


data = {
    "venueId": "03681010-10c5-4fd5-a7fa-27532d1059dc",
    "password": "960663"
}

# schedule = "09"
schedule = "20"

#暂时不抢二号场
course_2_flag = False
course_3_flag = False
course_4_flag = True
# 获取当前时间的小时数（24小时制）
login("mahaibin")
print headers
current_hour = datetime.now().hour
while current_hour > 5:
    print("当前时间是 %s，大于凌晨5点，开始循环等待..." % datetime.now())
    time.sleep(3)
    current_hour = datetime.now().hour
time.sleep(15)
while True:
    if course_2_flag:
        code1 = book_course("course_2", schedule,data)
        if code1 == 0:
            print(u"场次2抢到")
            break
        elif code1 == 22:
            course_2_flag = False
    if course_3_flag:
        code2 = book_course("course_3", schedule,data)
        if code2 == 0:
            print(u"场次3抢到")
            break
        elif code2 == 22:
            course_3_flag = False
    if course_4_flag:
        code3 = book_course("course_4", schedule,data)
        if code3 == 0:
            print(u"场次4抢到")
            break
        elif code3 == 22:
            course_4_flag = False
    if course_4_flag is not True and course_3_flag is not True and course_2_flag is not True:
        print(u"三个场都没有这个时间了，停止执行")
        break
    time.sleep(2)