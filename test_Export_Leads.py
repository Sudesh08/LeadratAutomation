from time import sleep

from Leadrat_FrameWork.pageObjects.exportLeads import ExportLeads
from Leadrat_FrameWork.pageObjects.login import log_in_Page


def test_Export_Leads(browserInstance):
    driver= browserInstance
    driver.get("https://prdrock.leadrat.com/login")
    logInPage=log_in_Page(driver)
    logInPage.logIn()
    sleep(5)

    leadExport=ExportLeads(driver)
    leadExport.leadExport()