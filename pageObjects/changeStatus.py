from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChangeStatus:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def clickOnStatusColumn(self):
        try:
            # Click the status column first
            change_status_column = self.driver.find_element(By.XPATH, "//div[@col-id='CustomLeadStatus']//p[1]")
            change_status_column.click()

            # Wait for options to load
            sleep(2)  # Or use WebDriverWait below if needed

            # Now locate and click the desired status option dynamically
            select_status = self.driver.find_element(By.XPATH, "//label[contains(@class, 'status-badge') and @for='leadOption0']")
            select_status.click()
            sleep(2)

            select_sub_status = self.driver.find_element(By.XPATH,"//label[contains(@class, 'status-badge') and @for='option1']")
            select_sub_status.click()
            sleep(2)

            self.driver.find_element(By.XPATH,"//textarea[@id='txtUpdateStatusNotes']").send_keys("I am writting notes on this")
            sleep(2)

            select_save_and_close = self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn-coal') and text()='Save and Close']")
            select_save_and_close.click()
            sleep(2)

            toaster_xpath = "//div[contains(@class, 'sn-title') and text()='Lead Status Updated Successfully']"
            try:
                toaster = self.wait.until(EC.visibility_of_element_located((By.XPATH, toaster_xpath)))
                print("✅ Lead Status validated: 'Lead Status Change Sucessfully' toast is visible.")
                return True
            except Exception as e:
                print(f"Error: {e}"+"\n Status not changed")
                return False

        except Exception as e:
            print(f"Error clicking status column: {e}")
