from anyio import sleep

from Leadrat_FrameWork.pageObjects.AddLead import AddLead
from Leadrat_FrameWork.pageObjects.login import log_in_Page


def test_AddLead(browserInstance):
    driver= browserInstance
    driver.get("https://prdrock.leadrat.com/login")
    logInPage=log_in_Page(driver)
    logInPage.logIn()

    add_Lead_Button=AddLead(driver)
    add_Lead_Button.Add_Lead()
