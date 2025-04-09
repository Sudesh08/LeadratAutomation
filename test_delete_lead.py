from time import sleep

from Leadrat_FrameWork.pageObjects.Delete_Lead import DeleteLead
from Leadrat_FrameWork.pageObjects.login import log_in_Page


def test_LogIn(browserInstance):
    driver= browserInstance
    driver.get("https://prdrock.leadrat.com/login")
    logInPage=log_in_Page(driver)
    logInPage.logIn()

    deleteLead = DeleteLead(driver)
    deleteLead.deleteLead()
    sleep(5)