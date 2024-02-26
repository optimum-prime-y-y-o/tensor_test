import pytest
from selenium import webdriver
import logging

@pytest.fixture()
def browser():
    logging.info("Started")

    driver = webdriver.Chrome()
    driver.get("https://sbis.ru/")
    yield driver
    driver.quit()