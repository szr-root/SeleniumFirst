from selenium import webdriver


class TestDebug:

    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=chrome_args)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_debug(self):
        self.driver.find_element_by_id("menu_customer").click()
