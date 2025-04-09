from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Leadrat_FrameWork.pageObjects.Delete_Lead import DeleteLead
from Leadrat_FrameWork.pageObjects.login import log_in_Page


def test_LogIn(browserInstance):
    driver = browserInstance
    try:
        driver.get("https://prdrock.leadrat.com/login")

        # Login
        login_page = log_in_Page(driver)
        login_page.logIn()

        # Delete lead
        delete_lead = DeleteLead(driver)
        delete_lead.deleteLead()  # This clicks the delete icon

        # Wait for and click the confirmation "Yes" button
        yes_button = (By.XPATH, "//button[@id='deleteYes' and @data-automate-id='deleteYes']")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(yes_button)
        ).click()

        # Add verification/assertion here if needed
        # For example, wait for success message or lead to be removed

    except Exception as e:
        print(f"Error during test execution: {str(e)}")
        raise
    finally:
        driver.quit()