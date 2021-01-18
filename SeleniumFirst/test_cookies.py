import json
from time import sleep

from selenium import webdriver


class TestCookies:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_cookies(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element_by_xpath("//*[@id='indexTop']/div[2]/aside/a[1]").click()
        sleep(15)
        cookies = self.driver.get_cookies()
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)


        # self.driver.get("https://work.weixin.qq.com/")
        # with open("cookie.json", "r")as f:
        #     cookies = json.load(f)
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # self.driver.find_element_by_id("menu_customer").click()

