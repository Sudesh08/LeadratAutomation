from time import sleep

from Leadrat_FrameWork.pageObjects.documentUpload import leadDocumentUpload
from Leadrat_FrameWork.pageObjects.login import log_in_Page


def test_LogIn(browserInstance):
    driver= browserInstance
    driver.get("https://prdrock.leadrat.com/login")
    logInPage=log_in_Page(driver)
    logInPage.logIn()

    clickDocumentUpload = leadDocumentUpload(driver)
    clickDocumentUpload.lead_Document_Upload()
    sleep(5)