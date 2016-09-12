#-*- coding: utf-8 -*-
import datetime


def create_prefics():
    now = datetime.datetime.now()
    now_date = now.month() + "" + now.day()
    now_time = now.hour() + "" + now.minute()
    return now_date + '' + now_time


def test_search_in_python_org(app):
    app.open_home_page()
    app.enter_authorization()
    # app.authorization.login("akordyukova@pronto.ru", "111111")
    app.authorization.login("test.stage@pronto.ru", "111111")
    app.logo_click()
    app.authorization.logout()




