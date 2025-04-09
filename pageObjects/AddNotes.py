from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class addNotes:
    def __init__(self, driver):
        self.driver = driver
        self.addNotesIcon = (By.XPATH, "//span[@class='icon ic-notes m-auto ic-xxs']")
        self.addNotesValue = (By.XPATH, "//input[@formcontrolname='notes' and @placeholder='Type here....']")
        self.clickSubmit = (By.XPATH, "//span[contains(@class, 'ic-tick') and contains(@class, 'icon')]")

    def add_Notes(self):
        try:
            # Wait for the 'Add Notes' icon to be clickable
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.addNotesIcon)
            ).click()

            # Wait for the input field to be clickable and send keys
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.addNotesValue)
            ).send_keys("Some notes I am writing here")

            # Wait for the submit icon to be clickable and click it
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.clickSubmit)
            ).click()

        except Exception as e:
            print(f"Something Went Wrong: {e}")
