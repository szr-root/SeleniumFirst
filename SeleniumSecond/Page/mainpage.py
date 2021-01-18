from SeleniumSecond.Page.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from SeleniumSecond.Page.contactpage import ContactPage


class MainPage(BasePage):
    def goto_adddepartment_page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".frame_nav a:nth-child(2)").click()
        return ContactPage(self.driver)
