#-*- coding: utf-8 -*-


def test_search_in_python_org(app):
    app.open_home_page()
    app.authorization.login("akordyukova@pronto.ru", "111111")
    app.wd.get("http://irr.ru")
    app.authorization.logout()





