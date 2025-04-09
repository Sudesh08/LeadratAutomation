from time import sleep

from Leadrat_FrameWork.pageObjects.changeStatus import ChangeStatus
from Leadrat_FrameWork.pageObjects.login import log_in_Page


def testChangeStatus(browserInstance):
    driver = browserInstance
    driver.get("https://prdrock.leadrat.com/login")

    logInPage = log_in_Page(driver)
    logInPage.logIn()
    sleep(5)

    change_Status_Method=ChangeStatus(driver)
    change_Status_Method.clickOnStatusColumn()