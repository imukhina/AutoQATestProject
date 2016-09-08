
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def login(self, login_name, password):
        wd = self.wd
        self.enter_authorization()
        wd.find_element_by_name("login").send_keys(login_name)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_class_name("js-authFormLogin").submit()
        WebDriverWait(self.wd, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "user-account")))
        assert "http://irr.ru/account/items" == self.wd.current_url

    def enter_authorization(self):
        wd = self.wd
        wd.find_element_by_class_name("js-authorizationButton").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://irr.ru")

    def destroy(self):
        self.wd.quit()



