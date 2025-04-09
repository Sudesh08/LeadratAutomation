from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DeleteLead:
    def __init__(self, driver):
        self.driver = driver
        self.deleteleadClickActionButton = (By.XPATH, "//span[@id='clkDeleteLead' and @data-automate-id='clkDeleteLead' and contains(@class, 'icon') and contains(@class, 'ic-delete')]")

    def delete_lead(self):
        try:
            # Click the delete button
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.deleteleadClickActionButton)
            ).click()

            # Wait for and click the confirmation "Yes" button
            yes_button = (By.XPATH, "//button[@id='deleteYes' and @data-automate-id='deleteYes']")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(yes_button)
            ).click()

            # Add verification/assertion here if needed
            # For example, wait for success message or lead to be removed
        except Exception as e:
            print(f"Error during test execution: {str(e)}")
            raise
