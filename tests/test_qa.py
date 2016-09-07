#-*- coding: utf-8 -*-
import unittest


import pytest

from application import Application

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy())
    return fixture



def test_search_in_python_org(self):
    app.open_home_page()
    app.login( login_name="akordyukova@pronto.ru", password="111111")



