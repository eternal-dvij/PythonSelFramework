from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    # self.driver.find_elements(By.XPATH, "//div[@class='card h-100/div/h4/a']")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")

    checkoutItems = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")

    checkoutBtn = (By.XPATH, "//button[@class='btn btn-success']")
    # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']")

    def getcardTitle(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getcardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkoutItem(self):
        return self.driver.find_element(*CheckoutPage.checkoutItems)

    def checkoutButton(self):
        self.driver.find_element(*CheckoutPage.checkoutBtn).click()
        confirmpg = ConfirmPage(self.driver)
        return confirmpg