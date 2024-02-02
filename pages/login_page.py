from selenium.webdriver.common.by import By
from pages.base_page import Base_Page

class LoginPage(Base_Page):
 
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    adactin_logo = (By.CSS_SELECTOR, ".logo")
    username = (By.CSS_SELECTOR, "#username")
    password = (By.CSS_SELECTOR, "#password")
    login_button = (By.CSS_SELECTOR, "#login")
    error_message = (By.CSS_SELECTOR, ".auth_error>b")

    def login(self, username, password):
        self.input_text(self.username, username)
        self.input_text(self.password, password)
        self.click_element(self.login_button)
    
    def login_screen(self):
        self.wait_untill_element_present(self.adactin_logo, 30)
        self.page_should_contains_element(self.adactin_logo)

    def login_error_message(self):
        self.wait_untill_element_present(self.error_message, 30)
        text = self.exeute_java_script("document.querySelector('.auth_error>b').innerText")
        print(text)
        # assert text == "'Invalid Login details or Your Password might have expired. Click here to reset your password'"