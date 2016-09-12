#import untangle
#import argparse

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from source.auth_source import Authorization


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.authorization = Authorization(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://irr.ru.stage/")

    def logo_click(self):
        wd = self.wd
        if wd.current_url == "http://irr.ru.stage/":
            wd.find_element_by_class_name("header__item").click()
        else:
            if wd.current_url == "http://irr.ru.stage/account/items":
                wd.find_element_by_css_selector(".navbar_account-logo").click()

        WebDriverWait(self.wd, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "header__inputHolder")))
        assert self.wd.current_url == "http://irr.ru.stage/"

    def enter_authorization(self):
        wd = self.wd
        wd.find_element_by_class_name("js-authorizationButton").click()

    def destroy(self):
        self.wd.quit()



