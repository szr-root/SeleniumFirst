from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from SeleniumSecond.Page.basepage import BasePage


class ContactPage(BasePage):
    def add_department(self):
        self.driver.find_element(By.CSS_SELECTOR, ".js_create_dropdown").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js_create_party").click()
        self.driver.find_element(By.NAME, "name").send_keys("坑钱部")
        self.driver.find_element(By.CSS_SELECTOR, ".js_parent_party_name").click()
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688851105560052_anchor']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[d_ck=submit]").click()
        self.driver.refresh()
        return self

    def add_department_fail(self):
        self.driver.find_element(By.CSS_SELECTOR, ".js_create_dropdown").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js_create_party").click()
        self.driver.find_element(By.NAME, "name").send_keys("坑钱部")
        self.driver.find_element(By.CSS_SELECTOR, ".js_parent_party_name").click()
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688851105560052_anchor']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[d_ck=submit]").click()
        return self

    def get_department_list(self):
        department_element_list = self.driver.find_elements(By.CSS_SELECTOR, ".jstree-anchor")
        department_list = []
        for depelement in department_element_list:
            department_list.append(depelement.text)
        return department_list

    def get_toast(self):
        toast = self.driver.find_element(By.XPATH, '//*[@id="js_tips"]')
        toast = toast.text
        return toast