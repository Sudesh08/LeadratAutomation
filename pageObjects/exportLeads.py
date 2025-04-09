from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ExportLeads:
    def __init__(self, driver):
        self.driver = driver
        # Locator for the Export button
        self.click_onExport_Button = (By.XPATH, "//div[contains(@class, 'bg-accent-green') and normalize-space(text())='Export']")
        self.click_Confirm_Button = (By.XPATH, "//button[@class='btn-coal ml-10' and normalize-space(text())='Confirm']")


    def leadExport(self):
        try:
            # Use the correct locator here
            self.driver.find_element(*self.click_onExport_Button).click()
            sleep(5)

            self.driver.find_element(*self.click_Confirm_Button).click()
            sleep(5)

            toaster_xpath = "//div[@class='sn-title ng-tns-c54-2 ng-star-inserted' and normalize-space(text())='Leads are being exported in excel format']"
            try:
                toaster = self.wait.until(EC.visibility_of_element_located((By.XPATH, toaster_xpath)))
                print("✅Export  Sucessfully' toast is visible.")
                return True
            except Exception as e:
                print(f"Error: {e}" + "\n Export not done")
                return False

        except Exception as e:
            print(f"Error clicking status column: {e}")
