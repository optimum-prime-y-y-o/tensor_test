
class BasePage():

    def __init__(self,browser):
        self.browser = browser

    def go_to_url(self,url):
        self.browser.get(url)