import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://www.makemytrip.global/?cc=de")
    time.sleep(5)
    #acceptbutton = wait.until(EC.presence_of_element_located(By.XPATH, "//button[normalize-space()='ACCEPT']"))
    acceptbutton = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='ACCEPT']")))

    acceptbutton.click()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    time.sleep(5)
    driver.quit()




