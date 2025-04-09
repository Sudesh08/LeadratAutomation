from time import sleep

from Leadrat_FrameWork.pageObjects.AddNotes import addNotes
from Leadrat_FrameWork.pageObjects.edit_Lead import EditLead
from Leadrat_FrameWork.pageObjects.login import log_in_Page


def test_LogIn(browserInstance):
    driver= browserInstance
    driver.get("https://prdrock.leadrat.com/login")
    logInPage=log_in_Page(driver)
    logInPage.logIn()

    add_Notes = addNotes(driver)
    add_Notes.add_Notes()
    sleep(5)