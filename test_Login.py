
import time
from selenium.webdriver.common.by import By

from Leadrat_FrameWork.pageObjects.AddLead import AddLead
from Leadrat_FrameWork.pageObjects.leadPage import LeadPage
from Leadrat_FrameWork.pageObjects.login import log_in_Page


def test_LogIn(browserInstance):
    driver= browserInstance
    driver.get("https://prdrock.leadrat.com/login")
    logInPage=log_in_Page(driver)
    logInPage.logIn()

    lead_page = LeadPage(driver)
    assert lead_page.is_on_manage_leads_page(), "Not on Manage Leads page"
