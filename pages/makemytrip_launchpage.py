import time
import pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class launchpage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    #loactors list
    roundtripbuttonlocator ="//li[@data-cy='roundTrip']"


    def roundtripbutton(self):
        #wait = WebDriverWait(self.driver, 10)
        roundtrip = self.wait.until(EC.presence_of_element_located((By.XPATH, "//li[@data-cy='roundTrip']")))
        #roundtrip = self.wait.until(EC.presence_of_element_located((By.XPATH, roundtripbuttonlocator)))
        roundtrip.click()
        time.sleep(3)

    '''
    def departfrom(self):
        wait = WebDriverWait(self.driver, 10)
        departure = self.driver.find_element(By.XPATH, "//input[@id='fromCity']")
        departure.click()
        departure_box = self.driver.find_element(By.XPATH, "//input[@placeholder='From']")
        time.sleep(3)
        departure_box.send_keys("mumbai")
        time.sleep(3)
        departure_box.send_keys(Keys.ARROW_DOWN)
        departure_box.send_keys(Keys.ENTER)
        time.sleep(3)
    '''
    def departfrom(self):
        #wait = WebDriverWait(self.driver, 10)
        departure = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='fromCity']")))
        departure.click()
        departure_box = self.wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='From']")))
        departure_box.send_keys("mumbai")
        time.sleep(2)
        departure_box.send_keys(Keys.ARROW_DOWN)
        departure_box.send_keys(Keys.ENTER)
        time.sleep(3)


    arrive_to_box = "//input[@id='toCity']"
    arrival_location_box = "//input[@placeholder='To']"


    def get_arrive_field(self):
        #wait = WebDriverWait(self.driver, 10)
        return  self.wait.until(EC.presence_of_element_located((By.XPATH, self.arrive_to_box )))

    def give_arrive_location(self):
        #wait = WebDriverWait(self.driver, 10)
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.arrival_location_box)))

    def enter_arrive_location(self, enter_location):
        self.get_arrive_field().click()
        time.sleep(3)
        self.give_arrive_location().send_keys(enter_location)
        time.sleep(3)
        self.give_arrive_location().send_keys(Keys.ARROW_DOWN)
        self.give_arrive_location().send_keys(Keys.ENTER)
        #self.get_arrive_field()
        
    '''

    def arrive(self, selectarrivalpoint):
        arrival = self.driver.find_element(By.XPATH, "//input[@id='toCity']")
        arrival.click()
        arrival_box = self.driver.find_element(By.XPATH, "//input[@placeholder='To']")
        arrival_box.send_keys(selectarrivalpoint)
        time.sleep(3)
        arrival_box.send_keys(Keys.ARROW_DOWN)
        arrival_box.send_keys(Keys.ENTER)
        time.sleep(3)
    '''


    def selectdatehere(self):
        #wait = WebDriverWait(self.driver, 10)
        departure_date = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='DayPicker-Day' and @aria-label='Wed Jul 30 2025']")))
         #departure_date = self.driver.find_element(By.XPATH,"//div[@class='DayPicker-Day' and @aria-label='Wed Jul 30 2025']")
        chains = ActionChains(self.driver)
        time.sleep(5)
        chains.move_to_element(departure_date).perform()
        time.sleep(2)
        departure_date.click()

        return_date = self.driver.find_element(By.XPATH, "//div[@class='DayPicker-Day' and @aria-label='Sat Aug 23 2025']")
        return_date.click()
        time.sleep(5)


    def searchbox(self):
        searchbox = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Search']")))
        #searchbox = self.driver.find_element(By.XPATH, "//a[normalize-space()='Search']")
        searchbox.click()


