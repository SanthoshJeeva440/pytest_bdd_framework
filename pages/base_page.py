from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base_Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def input_text(self, by_locator, text):
        self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(text)

    def click_element(self, by_locator):
        self.driver
        self.wait.until(EC.presence_of_element_located(by_locator)).click()

    def clear_text(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).clear()

    def wait_untill_element_present(self, by_locator, time=10):
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(by_locator))

    def page_should_contains_element(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator))
    
    def exeute_java_script(self, script):
        self.driver.execute_script(script)