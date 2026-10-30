from pages.homepage import HomePage
from pages.product import ProductPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    productpage = ProductPage(driver)
    productpage.check_title_is_('Samsung galaxy s6')
    
def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_products()
    WebDriverWait(driver, 10).until(
        lambda browser: len(browser.find_elements(
            By.XPATH, "//div[@id='tbodyid']/div"
        )) == 2
    )
    homepage.check_products_count_(2)
    