from selenium.webdriver.common.by import By
import logging

from pages.base_page import BasePage
from pages.sbis_contact_page import SbisContactsPage
from pages.sbis_download_page import SbisDownloadPage

class SbisMainPageLocators():
    LOCATOR_CONTACTS = (By.XPATH,"//a[@href='/contacts' and contains(@class, 'sbisru-Header__menu-link')]")
    LOCATOR_DOWNLOAD = (By.LINK_TEXT,"Скачать локальные версии") # Скачать СБИС

class SbisMainPage(BasePage):

    def go_to_contact_page(self):
        contacts_link = self.browser.find_element(*SbisMainPageLocators.LOCATOR_CONTACTS)
        url = contacts_link.get_attribute('href')
        self.go_to_url(url)

        logging.info("Выполнен переход на страницу с контактами")
        return SbisContactsPage(self.browser)
    
    def go_to_download_page(self):
        download_page_url = self.browser.find_element(*SbisMainPageLocators.LOCATOR_DOWNLOAD)
        download_page_url = download_page_url.get_attribute('href')
        self.go_to_url(download_page_url)

        logging.info("Выполнен переход на страницу с загрузками")
        return SbisDownloadPage(self.browser)
        