from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Leadrat_FrameWork.pageObjects.AddLead import AddLead


class EditLead:
    def __init__(self, driver):
        self.driver = driver
        self.editleadClickActionButton = (By.XPATH, "//span[@id='clkEditLead' and @data-automate-id='clkEditLead' and contains(@class, 'icon') and contains(@class, 'ic-pen')]")
        self.primary_Number_Edit_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        self.AddLead = AddLead(driver)
        self.save_lead_Button=(By.XPATH,"//span[contains(@class, 'ng-star-inserted') and contains(text(), 'Save')]")


    def editLeadForm(self):
        try:
            # Wait for the element to be clickable before clicking it
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.editleadClickActionButton)
            ).click()
            sleep(5)

            # Clear the existing value in the primary number input field
            primary_number_input = self.driver.find_element(*self.primary_Number_Edit_input)
            primary_number_input.clear()  # This removes the existing value

            # Now enter the new value
            primary_number_input.send_keys(self.AddLead.generate_random_phone_number())
            sleep(5)

            self.driver.find_element(*self.save_lead_Button).click()
            sleep(5)

        except Exception as e:
            print(f"Something Went Wrong: {e}")
