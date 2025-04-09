from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddLead:
    def __init__(self, driver):
        self.driver = driver
        #Add Lead Button
        # self.addleadButton = (By.XPATH, "//a[contains(text(),'Add Lead')]")


        self.name_input = (By.XPATH, "//input[@id='inpLeadName']")

        # Fixed XPath for primary number input
        self.primary_Number_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")

        self.alternate_Number_input = (By.XPATH, "(//input[@type='tel' and contains(@class, 'mat-input-element')])[2]")

        self.email_input = (By.XPATH, "//input[@id='inpLeadMail']")
        # Fixed XPath for referral name input
        self.referralName_input = (By.XPATH, "//input[@id='inpReferralName']")

        self.referral_Number_input = (By.XPATH, "(//input[@type='tel' and contains(@class, 'mat-input-element')])[3]")

        self.referral_emai_input = (By.XPATH, "//input[@id='inpReferralMail']")

        # self.source_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")

        # self.primary_Owner_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")

        # self.secondary_Owner_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")

        self.min_Budget_input = (By.XPATH, "//input[@id='inpLeadLowerBudget']")

        self.max_Budget_input = (By.XPATH, "//input[@id='inpLeadUpperBudget']")

        self.carpet_Number_input = (By.XPATH, "//input[@formcontrolname='carpetArea']")

        self.buildUP_Number_input = (By.XPATH, "//input[@formcontrolname='builtUpArea']")
        self.Saleable_Area_input = (By.XPATH, "//input[@formcontrolname='saleableArea']")
        self.property_Area_input = (By.XPATH, "//input[@formcontrolname='propertyArea']")
        self.net_Area_input = (By.XPATH, "//input[@formcontrolname='netArea']")
        self.unit_Number_input = (By.XPATH, "//input[@formcontrolname='unitName']")
        self.cluster_Name_input = (By.XPATH, "//input[@formcontrolname='clusterName']")
        # self.purpose_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        # self.enquired_For_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        # self.property_Type_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        # self.property_Sub_Type_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        # self.project_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        # self.property_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        # self.offering_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        # self.agency_Name_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        # self.campaign_Name_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        # self.channnel_Partner_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        # self.possession_needed_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        self.company_Name_input = (By.XPATH, "//input[@formcontrolname='companyName']")
        self.designation_Name_input = (By.XPATH, "//input[@formcontrolname='designation']")
        # self.nastionality_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        # self.sourcing_Manager_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        # self.closing_Manager_input = (By.XPATH, "//input[@type='tel' and contains(@class, 'mat-input-element')]")
        self.executive_Name_input = (By.XPATH, "//input[@formcontrolname='channelPartnerExecutiveName']")
        self.executive_Number_input = (By.XPATH, "(//input[@type='tel' and contains(@class, 'mat-input-element')])[4]")
        # self.Notes_input = (By.XPATH, "//input[@formcontrolname='notes']")
        self.save_lead_Button=(By.XPATH,"//span[contains(@class, 'ng-star-inserted') and contains(text(), 'Save')]")

    def generate_random_name(self):
        def random_string(length):
            return ''.join(random.choices(string.ascii_uppercase, k=length))

        self.first_name = random_string(random.randint(3, 8))
        self.last_name = random_string(random.randint(3, 8))

    import random

    def generate_random_phone_number(self):
        # The first digit of the phone number cannot be zero for most countries
        first_digit = random.choice([7, 8, 9])  # Common starting digits in India, can be adjusted based on country
        # Generate the remaining 9 digits
        remaining_digits = ''.join(random.choices('0123456789', k=9))

        # Concatenate the first digit with the rest of the digits to form the full phone number
        return str(first_digit) + remaining_digits

    def Add_Lead(self):
        try:
            self.generate_random_name()
            self.generate_random_phone_number()
            # self.driver.find_element(By.XPATH, "//span[text()='Add Lead']").click()
            # sleep(1)  # Give form a moment to render
            wait = WebDriverWait(self.driver, 10)

            # Wait for 'Add Lead' button and click it
            add_lead_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Add Lead']")))
            add_lead_button.click()


            self.driver.find_element(*self.name_input).send_keys(self.first_name + " " + self.last_name)
            sleep(1)

            self.driver.find_element(*self.primary_Number_input).send_keys(self.generate_random_phone_number())
            sleep(1)

            self.driver.find_element(*self.alternate_Number_input).send_keys(self.generate_random_phone_number())
            sleep(1)

            self.driver.find_element(*self.email_input).send_keys("test@gmail.com")
            sleep(1)

            self.driver.find_element(*self.referralName_input).send_keys("Referral name")
            # sleep(1)

            self.driver.find_element(*self.referral_Number_input).send_keys("7766556677")
            # sleep(1)

            self.driver.find_element(*self.referral_emai_input).send_keys("referral@gmail.com")
            # sleep(1)

            # self.driver.find_element(*self.source_input).send_keys("9876675432")
            # sleep(1)

            # self.driver.find_element(*self.primary_Owner_input).send_keys("9876675432")
            # sleep(1)

            # self.driver.find_element(*self.secondary_Owner_input).send_keys(self.first_name)
            # sleep(1)

            self.driver.find_element(*self.min_Budget_input).send_keys("8938")
            # sleep(1)

            self.driver.find_element(*self.max_Budget_input).send_keys("98766")
            # sleep(1)

            self.driver.find_element(*self.carpet_Number_input).send_keys("767")
            # sleep(1)

            self.driver.find_element(*self.buildUP_Number_input).send_keys("234")
            # sleep(1)

            self.driver.find_element(*self.Saleable_Area_input).send_keys("987")
            # sleep(1)

            self.driver.find_element(*self.property_Area_input).send_keys("432")
            # sleep(1)

            self.driver.find_element(*self.net_Area_input).send_keys("6743")
            # sleep(1)

            self.driver.find_element(*self.unit_Number_input).send_keys("9898")
            # sleep(1)

            self.driver.find_element(*self.cluster_Name_input).send_keys("Sudesh Cluster")
            # sleep(1)

            self.driver.find_element(*self.company_Name_input).send_keys("Leadrat")
            # sleep(1)

            self.driver.find_element(*self.designation_Name_input).send_keys("Automation Tester")
            # sleep(1)

            self.driver.find_element(*self.executive_Name_input).send_keys("Sudesh Executive")
            # sleep(1)

            self.driver.find_element(*self.executive_Number_input).send_keys("9899988128")
            # sleep(1)

            # self.driver.find_element(*self.Notes_input).send_keys("Notes")
            # # sleep(1)

            self.driver.find_element(*self.save_lead_Button).click()
            sleep(5)

            toaster_xpath = "//div[contains(@class, 'sn-title') and contains(text(), 'Lead added Successfully')]"
            try:
                toaster = wait.until(EC.visibility_of_element_located((By.XPATH, toaster_xpath)))
                print("✅ Lead creation validated: 'Lead added Successfully' toast is visible.")
                return True
            except Exception as e:
                print(f"Error: {e}"+"\n Lead not created")
                return False

        except Exception as e:
            print(f"Error: {e}")
            return False
