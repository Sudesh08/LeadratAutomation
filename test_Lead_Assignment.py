from time import sleep

from Leadrat_FrameWork.pageObjects.leadAssignment import leadAssignment
from Leadrat_FrameWork.pageObjects.login import log_in_Page


def test_AddLead(browserInstance):
    driver= browserInstance
    driver.get("https://prdrock.leadrat.com/login")
    logInPage=log_in_Page(driver)
    logInPage.logIn()
    sleep(5)

    leadAssignmentColumn=leadAssignment(driver)
    leadAssignmentColumn.implementLeadAssignment()