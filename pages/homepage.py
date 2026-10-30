from selenium.webdriver.common.by import By

class HomePage:
    
    def __init__(self, driver):
        self.driver = driver
    
    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, "//a[text()='Samsung galaxy s6']")
        galaxy_s6.click()
        
    def click_products(self):
        link = self.driver.find_element(By.XPATH, "//a[@id='itemc' and text()='Monitors']")
        link.click()
        
    def check_products_count_(self, count):
        cards = self.driver.find_elements(By.XPATH, "//div[@id='tbodyid']/div")
        assert len(cards) == count
    
    def open(self):
        self.driver.get("https://demoblaze.com/index.html")