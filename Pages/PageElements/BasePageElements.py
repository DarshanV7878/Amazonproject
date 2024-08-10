from selenium.webdriver.chrome import webdriver
from Pages.PagesObjects.locatormethods import LocatorCommonMethods


class BasePageElements(LocatorCommonMethods):

    def __init__(self, driver: webdriver):
        self.driver = driver
