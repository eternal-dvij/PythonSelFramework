from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    country = (By.ID, "country")
    # self.driver.find_element(By.ID, "country").

    agreeterms = (By.XPATH, "//label[contains(text(), 'I agree with the')]")

    purchasebtn = (By.CSS_SELECTOR, ".btn-lg")
    # self.driver.find_element(By.CSS_SELECTOR, ".btn-lg")

    def inputCountryName(self):
        return self.driver.find_element(*ConfirmPage.country)

    def agreetermsandcodition(self):
        return self.driver.find_element(*ConfirmPage.agreeterms)

    def purchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchasebtn)