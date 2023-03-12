from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.XPATH, "//a[contains(@href,'shop')]")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkicecream = (By.ID, "exampleCheck1")
    student = (By.CSS_SELECTOR, "#inlineRadio1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")

    def __init__(self,driver):
        self.driver = driver

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage
        # driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def checkbox(self):
        return self.driver.find_element(*HomePage.checkicecream)

    def setStudent(self):
        return self.driver.find_element(*HomePage.student)

    def selectgender(self,):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.alert)