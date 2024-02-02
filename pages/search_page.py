from pages.base_page import Base_Page
import time
from selenium.webdriver.common.by import By

class SearchPage(Base_Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    search_hotel = (By.CSS_SELECTOR, ".login_title")
    logout_button = (By.CSS_SELECTOR, ".welcome_menu>a:nth-child(5)")
    again_login_button = (By.CSS_SELECTOR, ".reg_success>a")

    def search_hotel_screen(self):
        time.sleep(2)
        self.wait_untill_element_present(self.search_hotel, 30)
        self.page_should_contains_element(self.search_hotel)

    def logout(self):
        self.page_should_contains_element(self.logout_button)
        self.click_element(self.logout_button)

    def again_login(self):
        self.wait_untill_element_present(self.again_login_button)
        self.click_element(self.again_login_button)