from anyio import sleep
from selenium.webdriver.common.by import By


class log_in_Page:
    def __init__(self,driver):
        self.driver = driver
        self.username_input = (By.ID, "inpLoginName")
        self.password_input = (By.ID, "inpLoginPassword")
        self.login_button = (By.CLASS_NAME, "btn-accent-green-xl")

    def logIn(self):
        self.driver.find_element(*self.username_input).send_keys("raina87")
        self.driver.find_element(*self.password_input).send_keys("Sudesh001@")
        self.driver.find_element(*self.login_button).click()
        sleep(5)

