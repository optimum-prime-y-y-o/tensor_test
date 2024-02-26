from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from pages.base_page import BasePage
from pages.tensor_about_page import TensorAboutPage

class TensorMainPageLocators():
    LOCATOR_STRENGTH_PEOPLE_BLOCK = (By.CLASS_NAME,"tensor_ru-Index__block4-content")
    LOCATOR_ABOUT = (By.XPATH, "//div[contains(@class,'tensor_ru-Index__block4-content')]/descendant::a")


class TensorMainPage(BasePage):
    
    def valid_url(self):
        tensr_url = "https://tensor.ru/"
        url_valid = WebDriverWait(self.browser,5).until(EC.url_to_be(tensr_url))

        assert url_valid
        logging.info("url текущей страницы совпадает с ожидаемым")

    def have_strength_in_people_block(self):
        block_name = "Сила в людях"
        
        have_block = WebDriverWait(self.browser,5).until(
            EC.text_to_be_present_in_element(TensorMainPageLocators.LOCATOR_STRENGTH_PEOPLE_BLOCK,
                                             block_name)
            )
        
        assert have_block
        logging.info("На странице присутствует блок 'Сила в людях'")


    def go_to_about(self):
        about_in_block = self.browser.find_element(*TensorMainPageLocators.LOCATOR_ABOUT)
        url_from_block = about_in_block.get_attribute('href')

        self.go_to_url(url_from_block)
        logging.info("Выполнен переход на страницу Подробнее")
        return TensorAboutPage(self.browser)



        