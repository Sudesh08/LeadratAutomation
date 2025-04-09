import pyautogui
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class leadDocumentUpload:
    def __init__(self, driver):
        self.driver = driver
        self.leadDocumentUploadIcon = (By.XPATH, "//span[contains(@class, 'icon') and contains(@class, 'ic-upload')]")
        self.clickUploadNewDocument = (By.XPATH,
                                       "//div[contains(@class, 'btn-accent-green') and contains(@class, 'btn-md') and normalize-space(text())='Upload New Document']")
        self.documentNameInputField = (
            By.XPATH,
            "//input[@id='inpLeadsDoc' and @name='leadDocName' and @placeholder='Enter lead document name...']")
        self.clickOnBrowseButton = (By.XPATH, "//span[@id='uploadImages' and contains(@class, 'button-browse')]")
        self.fileInputField = (
        By.XPATH, "//input[@type='file']")  # This is the hidden input field where files are selected
        self.saveButton = (By.XPATH, "//button[contains(@class, 'btn-coal') and normalize-space(text())='Save']")

    def lead_Document_Upload(self):
        try:
            # Wait for the lead document upload icon to be clickable and click it
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.leadDocumentUploadIcon)
            ).click()

            # Wait for the 'Upload New Document' button and click it
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.clickUploadNewDocument)
            ).click()

            # Enter the document name
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.documentNameInputField)
            ).send_keys("Document 001")

            # Wait for the browse button and click it to open the file dialog
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.clickOnBrowseButton)
            ).click()

            # Wait for the file input dialog to open (usually takes a second)
            sleep(2)

            # Prepare the file path you want to upload
            file_path = r"C:\Users\sudes\OneDrive\Pictures\Screenshots\Image.png"

            # Copy the file path to clipboard
            pyperclip.copy(file_path)

            # Paste the file path in the file explorer dialog using ctrl+v
            pyautogui.hotkey('ctrl', 'v')

            # Press 'Enter' to upload the file
            pyautogui.press('enter')

            # Optional: wait for file upload to complete if necessary
            sleep(5)

            # Now click on the 'Save' button
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.saveButton)
            ).click()

            # Optional: wait for the save action to complete if needed
            sleep(3)

        except Exception as e:
            print(f"Something Went Wrong: {e}")

