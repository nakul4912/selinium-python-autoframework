import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.makemytrip_launchpage import launchpage

@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:
    def test_search_flights(self):

        lp = launchpage(self.driver, self.wait)
        """
        in this i have automated the flight booking followed as
        1 open the website
        2 accept the cookies
        3 select the  round trip option
        """

        lp.roundtripbutton()

#4 select the departure option
        lp.departfrom()
#5 select the arrival option

        lp.enter_arrive_location("budapest")

        #lp.arrive("budapest")
#6 select the departure date

        lp.selectdatehere()
#7 select the return date
        lp.searchbox()
#8 select the search botton
