from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from pages.base_page import BasePage
from pages.tensor_main_page import TensorMainPage

class SbisContactsPageLocators():
    LOCATOR_BANNER = (By.CLASS_NAME,"sbisru-Contacts__logo-tensor")
    LOCATOR_REGION = (By.XPATH,"//span[contains(@class,'sbis_ru-Region-Chooser__text')]")
    LOCATOR_PARTNERS = (By.NAME,"itemsContainer")
    LOCATOR_NEW_REGION = (By.XPATH, "//span[@title='Камчатский край']") #sbis_ru-Region-Panel__list-l")
    LOCATOR_PARTNERS_CITY_NAME = (By.ID, "city-id-2")

class SbisContactsPage(BasePage):
     
    def click_banner(self):
        banner = self.browser.find_element(*SbisContactsPageLocators.LOCATOR_BANNER)
        url = banner.get_attribute('href')
        assert url == "https://tensor.ru/"
        # banner.click()
        self.go_to_url(url)
        logging.info("Выполнен переход по баннеру")
        return TensorMainPage(self.browser)
    
    def check_default_region(self):
        region = "Республика Башкортостан"

        same_region = WebDriverWait(self.browser,5).until(
            EC.text_to_be_present_in_element(SbisContactsPageLocators.LOCATOR_REGION,
                                             region)
            )
        assert same_region
        logging.info("Регион определился правильно")

    def check_partners(self):
        partners = WebDriverWait(self.browser,5).until(
            EC.visibility_of_element_located(SbisContactsPageLocators.LOCATOR_PARTNERS))
        
        assert partners
        logging.info("Присутствует список партнеров")

    def change_region(self):

        region_panel = self.browser.find_element(*SbisContactsPageLocators.LOCATOR_REGION)
        region_panel.click()

        new_region = WebDriverWait(self.browser,5).until(
            EC.visibility_of_element_located(SbisContactsPageLocators.LOCATOR_NEW_REGION))

        new_region.click()
        logging.info("Выполнена смена региона")

    def check_new_region_url(self):
        need_in_url = "41-kamchatskij-kraj"
        url_valid = WebDriverWait(self.browser,5).until(EC.url_contains(need_in_url))

        assert url_valid
        logging.info("Измененный URL содержит информацию выбранного региона")
        
    def check_new_region_partners(self):
        need_region_name = "Петропавловск-Камчатский"

        current_city = WebDriverWait(self.browser,5).until(
            EC.text_to_be_present_in_element(SbisContactsPageLocators.LOCATOR_PARTNERS_CITY_NAME,
                                             need_region_name)
            )
        
        assert current_city
        logging.info("Измененный список партнеров содержит информацию выбранного региона")

    def check_new_region_name(self):
        region = "Камчатский край"

        same_region = WebDriverWait(self.browser,5).until(
            EC.text_to_be_present_in_element(SbisContactsPageLocators.LOCATOR_REGION,
                                             region)
            )
        
        assert same_region
        logging.info("Название региона изменилось на выбранный регион")

    def check_new_region_title(self):
        str_in_title = "Камчатский край"
        contain = WebDriverWait(self.browser,5).until(EC.title_contains(str_in_title))
        assert contain
        logging.info("Измененный title содержит название выбранного региона")
        