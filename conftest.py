import pytest
import src.data as data
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture(scope='function')
def driver():
    service = FirefoxService(executable_path="C:\Installed\Soft\WebDriverFirefox\geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    driver.get(data.main_page_url)
    yield driver
    driver.quit()
