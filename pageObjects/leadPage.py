from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeadPage:
    def __init__(self, driver):
        self.driver = driver
        self.manage_leads_header = (By.XPATH, "//h6[contains(@class, 'header-5') and contains(text(), 'Manage Leads')]")

    def is_on_manage_leads_page(self, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(self.manage_leads_header))
            header_text = element.text.strip()
            print(f"📍 Page Header Found: '{header_text}'")
            return header_text == "Manage Leads"
        except Exception as e:
            print(f"❌ Error while verifying Manage Leads page: {e}")
            return False
