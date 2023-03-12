import time

from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("navigating to the shop page from home page")
        checkOutPage = homepage.shopItem()
        log.info("getting all the card titles")
        cards = checkOutPage.getcardTitle()
        i = -1
        for card in cards:
            i = i+1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getcardFooter()[i].click()

        checkOutPage.checkoutItem().click()

        confirmpg = checkOutPage.checkoutButton()
        log.info("enetering country name as ind")
        confirmpg.inputCountryName().send_keys("ind")

        log.info("going to check if country clicked is india or not")

        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        time.sleep(3)
        confirmpg.agreetermsandcodition().click()

        # assert driver.find_element(By.XPATH,"//label[contains(text(), 'I agree with the')]").is_selected()
        confirmpg.purchaseButton().click()
        textmatch = self.driver.find_element(By.CSS_SELECTOR,".alert-success").text
        log.info("text received from application is: "+textmatch)
        assert "Success!" in self.driver.find_element(By.CLASS_NAME, "alert-success").text
        var = self.driver.find_element(By.ID, "country").get_attribute("value")
        log.info(var)
        time.sleep(5)
