from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from pages.base_page import BasePage

class TensorAboutLocators():
    LOCATOR_WORKING_PICTURES = (By.XPATH, "//img[contains(@class,'tensor_ru-About__block3')]")
    
class TensorAboutPage(BasePage):
    
    def valid_url(self):
        tensr_url = "https://tensor.ru/about"
        url_valid = WebDriverWait(self.browser,5).until(EC.url_to_be(tensr_url))

        assert url_valid
        logging.info("url текущей страницы совпадает с ожидаемым")

    def work_photos_same_height_and_width(self):
        working_pictures = self.browser.find_elements(*TensorAboutLocators.LOCATOR_WORKING_PICTURES)

        height_set = set()
        width_set = set()

        for picture in working_pictures:
            height_set.add(picture.get_attribute("height"))
            width_set.add(picture.get_attribute("width"))
        print(height_set,width_set)

        assert len(height_set) == len(width_set) == 1
        logging.info("В разделе Работаем все фотографии с одинаковой высотой и шириной")