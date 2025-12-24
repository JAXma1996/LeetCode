# -*- coding: utf
# import ssl-8 -*-
# utils.py
import json

import ssl
from datetime import datetime, timedelta
import urllib2
import cookielib

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "http://www.yanlordlife.cn",
    "Referer": "http://www.yanlordlife.cn/stadium/booking/03681010-10c5-4fd5-a7fa-27532d1059dc",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
}



course_id_map = {
    "course_2": "52510dba-7e49-452f-93bf-588aad6c30ef",
    "course_3": "939fd40c-bb38-41dd-b74c-7618be7d45b0",
    "course_4": "a76ba330-dd43-4d9c-888c-3e1864c9acc8"
}
schedule_time_map = {
    "08": "2a2acc85-8aff-49fc-9e59-f4bd83cdfac8",
    "09": "de2b6e47-db54-4b02-9c42-4a9310da8ef7",
    "10": "fb0a41e8-eef4-4ae8-b526-3d25b9437589",
    "16": "2f0f0103-2518-4a18-b697-aa5597830bab",
    "17": "fdf9c97c-bdd4-44fb-9aac-41f2861c68e4",
    "18": "5d860220-f300-4815-9ef6-438b6c41ab40",
    "19": "03a3d24f-5052-467e-b431-25a06091d876",
    "20": "0cefc30c-7da4-418f-8ca7-f101bc05c8cb",
    "21": "10476590-4a7a-425c-879e-c14c8a5ae66c",
    "22": "60386a33-c47f-43fe-9dc4-074d8dd777aa"
}


def book_course(course_id, schedule,data):
    # 获取当前日期（只包含年月日）
    current_date = datetime.now().date()
    # 计算六天后的日期
    future_date = current_date + timedelta(days=6)
    # 格式化为 YYYY-MM-DD 字符串
    date_str = future_date.strftime('%Y-%m-%d')

    schedules = list()
    schedules.append(schedule_time_map[schedule])
    data["courtId"] = course_id_map[course_id]
    data["bookingDate"] = date_str
    data["schedules"] = schedules

    try:

        context = ssl._create_unverified_context()

        request = urllib2.Request("http://www.yanlordlife.cn/api/front/club/venue/booking", json.dumps(data), headers)
        response = urllib2.urlopen(request, context=context,timeout=10)

        result = response.read()
        # result = '{"code":0,"message":"选择场次已被占用，不可以预订了"}'
        response_data = json.loads(result)

        code = response_data.get('code')
        message = response_data.get('message')
        # 获取当前日期和时间

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(u"时间：%s 场次：%s 预定时间段：%s code参数值：%d message参数值：%s"  % (current_time,course_id,schedule, code, message))
        if message == u"选择场次已被占用，不可以预订了" or message == u"工作日最多允许预定同一场馆2个场次":
            code = 22
        return code
    except urllib2.HTTPError as e:
        print("HTTP Error:", e.code, e.read())
        return 'fail'
    except urllib2.URLError as e:
        print("URL Error:", e.reason)
        return 'fail'
    except Exception as e:
        print("Other Error:", str(e))
        return 'fail'


def login(username):
    # 创建一个cookie处理器
    cookie_jar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))


    # 设置请求数据
    data = json.dumps({"username": username, "password": "123456"})

    # 发送请求
    try:
        request = urllib2.Request(
            url='http://www.yanlordlife.cn/api/front/member/login',
            data=data,
            headers=headers
        )
        response = opener.open(request)

        # 获取响应头中的Set-Cookie
        set_cookie = response.headers.getheader('Set-Cookie')
        print "原始Set-Cookie头信息:"
        print set_cookie

        # 从cookie jar中获取connect.sid
        connect_sid = None
        for cookie in cookie_jar:
            if cookie.name == 'connect.sid':
                connect_sid = cookie.value
                print "\n提取的connect.sid值:"
                print connect_sid
                headers["Cookie"] = "connect.sid=" + connect_sid
                break

        if not connect_sid:
            print "\n未找到connect.sid cookie"

    except urllib2.HTTPError as e:
        print "HTTP错误:", e.code
        print "错误信息:", e.read()
    except urllib2.URLError as e:
        print "URL错误:", e.reason
    except Exception as e:
        print "发生其他错误:", str(e)




# 场2：52510dba-7e49-452f-93bf-588aad6c30ef
# 场3：939fd40c-bb38-41dd-b74c-7618be7d45b0
# 场4：a76ba330-dd43-4d9c-888c-3e1864c9acc8
# {
#     "data": [
#         {
#             "id": 511,
#             "uuid": "be29b6df-7f85-4c63-90bf-3e2479367839",
#             "begin": "07:00",
#             "end": "08:00",
#             "price": "30.00",
#             "idle": true
#         },
#         {
#             "id": 512,
#             "uuid": "2a2acc85-8aff-49fc-9e59-f4bd83cdfac8",
#             "begin": "08:00",
#             "end": "09:00",
#             "price": "30.00",
#             "idle": false
#         },
#         {
#             "id": 513,
#             "uuid": "de2b6e47-db54-4b02-9c42-4a9310da8ef7",
#             "begin": "09:00",
#             "end": "10:00",
#             "price": "30.00",
#             "idle": false
#         },
#         {
#             "id": 514,
#             "uuid": "fb0a41e8-eef4-4ae8-b526-3d25b9437589",
#             "begin": "10:00",
#             "end": "11:00",
#             "price": "30.00",
#             "idle": false
#         },
#         {
#             "id": 515,
#             "uuid": "ccae2e63-b9bf-4f71-9d03-46df74a6f7f3",
#             "begin": "11:00",
#             "end": "12:00",
#             "price": "30.00",
#             "idle": false
#         },
#         {
#             "id": 516,
#             "uuid": "b57c9559-292b-4f60-aee6-a689c08c0919",
#             "begin": "12:00",
#             "end": "13:00",
#             "price": "30.00",
#             "idle": true
#         },
#         {
#             "id": 517,
#             "uuid": "889ab706-2e96-4cbc-8410-6ea58b991fa6",
#             "begin": "13:00",
#             "end": "14:00",
#             "price": "30.00",
#             "idle": true
#         },
#         {
#             "id": 518,
#             "uuid": "ed00bd7e-a876-4fe7-beb6-990c6fe3203a",
#             "begin": "14:00",
#             "end": "15:00",
#             "price": "30.00",
#             "idle": true
#         },
#         {
#             "id": 519,
#             "uuid": "9e72f77b-089c-4ed2-a2cc-69840fb08659",
#             "begin": "15:00",
#             "end": "16:00",
#             "price": "30.00",
#             "idle": true
#         },
#         {
#             "id": 520,
#             "uuid": "2f0f0103-2518-4a18-b697-aa5597830bab",
#             "begin": "16:00",
#             "end": "17:00",
#             "price": "30.00",
#             "idle": false
#         },
#         {
#             "id": 521,
#             "uuid": "fdf9c97c-bdd4-44fb-9aac-41f2861c68e4",
#             "begin": "17:00",
#             "end": "18:00",
#             "price": "30.00",
#             "idle": false
#         },
#         {
#             "id": 523,
#             "uuid": "5d860220-f300-4815-9ef6-438b6c41ab40",
#             "begin": "18:00",
#             "end": "19:00",
#             "price": "30.00",
#             "idle": false
#         },
#         {
#             "id": 522,
#             "uuid": "03a3d24f-5052-467e-b431-25a06091d876",
#             "begin": "19:00",
#             "end": "20:00",
#             "price": "30.00",
#             "idle": false
#         },
#         {
#             "id": 524,
#             "uuid": "0cefc30c-7da4-418f-8ca7-f101bc05c8cb",
#             "begin": "20:00",
#             "end": "21:00",
#             "price": "30.00",
#             "idle": false
#         },
#         {
#             "id": 525,
#             "uuid": "10476590-4a7a-425c-879e-c14c8a5ae66c",
#             "begin": "21:00",
#             "end": "22:00",
#             "price": "30.00",
#             "idle": false
#         },
#         {
#             "id": 526,
#             "uuid": "60386a33-c47f-43fe-9dc4-074d8dd777aa",
#             "begin": "22:00",
#             "end": "23:00",
#             "price": "30.00",
#             "idle": false
#         }
#     ],
#     "code": 0,
#     "message": "查询成功"
# }
