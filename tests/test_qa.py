#-*- coding: utf-8 -*-

import socket


s = socket.socket()
s.connect(("irr.ru", 80))



def test_search_in_python_org(app):
    app.open_home_page()
    app.login("akordyukova@pronto.ru", "111111")



