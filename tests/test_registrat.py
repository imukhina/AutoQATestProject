#-*- coding: utf-8 -*-
import datetime


def create_prefics():
    now = datetime.datetime.now()
    now_date = str(now.day) + str(now.month)
    now_time = str(now.hour) + str(now.minute)
    return now_date + '' + now_time

def test_simple_registration(app):
    app.open_home_page()
    app.enter_authorization()
    test_mail = "test+" + create_prefics() + "@pronto.ru"
    app.authorization.registration_regular(test_mail, "111111")

