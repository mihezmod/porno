from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        
    def check_title_is_(self, title):
        assert WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h2"), title)
        )