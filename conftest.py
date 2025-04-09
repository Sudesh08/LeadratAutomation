
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store" , default ="chrome" , help ="Browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name=request.config.getoption("browser_name")
    option = Options()
    option.add_argument("--disable-notifications")
    if browser_name=="chrome":
        driver = webdriver.Chrome(option)
        driver.maximize_window()
        # driver.implicitly_wait(5)
    elif browser_name=="firefox":
        firefox_options = FirefoxOptions()
        driver = webdriver.Firefox(firefox_options)
        driver.maximize_window()
        # driver.implicitly_wait(5)
    yield driver