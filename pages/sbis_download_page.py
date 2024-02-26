from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

from pages.base_page import BasePage
import logging
import os

class SbisDownloadPageLocators():
    LOCATOR_SBIS_PLUGIN = (By.XPATH, "//div[contains(@class,'controls-TabButtons')]/div[2]")
    LOCATOR_DOWNLOAD_FILE = (By.XPATH, "//a[contains(text(),'Скачать (Exe 8.16 МБ)')]")

class SbisDownloadPage(BasePage):
    
    def go_to_plugin(self):

        WebDriverWait(self.browser,10).until(
            EC.element_to_be_clickable(SbisDownloadPageLocators.LOCATOR_SBIS_PLUGIN)
            ).click()
        
        logging.info("Выполнен переход на страницу плагина")
    
    def download_plugin(self):

        url = self.browser.find_element(*SbisDownloadPageLocators.LOCATOR_DOWNLOAD_FILE).get_attribute("href")

        response = requests.get(url)
        with open('sbisplugin-setup-web.exe', 'wb') as file:
            file.write(response.content)
        
        logging.info("Выполненено скачивание плагина")

    def plugin_downloaded(self):
        assert os.path.isfile("sbisplugin-setup-web.exe")
        logging.info("Файл плагина присутствует в директории")
    
    def correct_plugin_size(self):
        size_on_page = 8.16

        file_size_bytes = os.path.getsize('sbisplugin-setup-web.exe')
        file_size_megabytes = file_size_bytes / 1048576

        assert size_on_page == round(file_size_megabytes,2)
        logging.info("Размер скачанного файла совпал с ожидаемым")