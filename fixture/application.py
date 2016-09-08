
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
        wd.get("http://irr.ru")

    def destroy(self):
        self.wd.quit()



