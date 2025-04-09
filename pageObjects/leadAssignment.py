from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class leadAssignment:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.assignToColumn=(By.XPATH,"//div[@col-id='AssignTo']//p[1]")
        self.buttonReAssign=(By.XPATH,"//button[contains(@class, 'btn') and text()=' Re-Assign Lead']")
        # This selects the ng-select container to click
        # self.dropdownClickArea = (By.XPATH, "//ng-select//div[contains(@class, 'ng-select-container')]")
        # self.searchValueForSecondary=(By.XPATH,"//input[@aria-autocomplete='list' and @type='text' and @autocorrect='off' and @autocapitalize='off' and @autocomplete='off']")
        # self.listOfUsers=(By.XPATH,"//div[@class='scrollable-content']//div[contains(@class, 'ng-option')]")
        self.assignmentSaveAndCloseButton=(By.XPATH,"//button[@class='btn-coal' and normalize-space(text())='Save and Close']")

    def implementLeadAssignment(self):
        try:
            self.driver.find_element(*self.assignToColumn).click()
            sleep(5)

            self.driver.find_element(*self.buttonReAssign).click()
            sleep(5)

        # WebDriverWait(self.driver, 5).until(
        #     EC.element_to_be_clickable(self.dropdownClickArea)
        # ).click()
        #
        # WebDriverWait(self.driver, 5).until(
        #     EC.element_to_be_clickable(self.searchValueForSecondary)
        # ).send_keys("ami")

            self.driver.find_element(*self.assignmentSaveAndCloseButton).click()
            sleep(5)


            # users_text = [user.text for user in self.listOfUsers]
            # print("Users in the dropdown:")
            # for user in users_text:
            #     print(user)
            # print("List of users " + str(len(self.listOfUsers)))
            # self.driver.find_element(*self.listOfUsers).click()
            toaster_xpath = "//div[contains(@class, 'sn-title') and contains(text(), 'Lead Assignment Updated Successfully')]"
            try:
                toaster = self.wait.until(EC.visibility_of_element_located((By.XPATH, toaster_xpath)))
                print("✅ Lead Status validated: 'Lead Status Change Sucessfully' toast is visible.")
                return True
            except Exception as e:
                print(f"Error: {e}" + "\n Status not changed")
                return False

        except Exception as e:
            print(f"Something Went Wrong: {e}")