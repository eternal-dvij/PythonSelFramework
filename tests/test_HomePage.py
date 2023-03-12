import time

import pytest
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):

    def test_formSubmission(self, getdata):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("firstname is :" + getdata["firstname"])
        homepage.getName().send_keys(getdata["firstname"])
        log.info("lastname is :" + getdata["lastname"])
        homepage.getEmail().send_keys(getdata["lastname"])
        homepage.getPassword().send_keys("abcd123")
        homepage.checkbox().click()
        homepage.setStudent().click()
        # static dropdown
        log.info("gender is :" + getdata["gender"])
        self.selectOptionBytext(homepage.selectgender(),getdata["gender"])
        homepage.submitForm().click()
        message = homepage.getSuccessMessage().text
        log.info(message)
        assert "Success" in message  # error
        time.sleep(7)
        self.driver.refresh()

    @pytest.fixture(params = HomePageData.getTestData("Testcase2"))
    def getdata(self,request):
        return request.param