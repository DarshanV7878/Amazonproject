from selenium.webdriver.chrome import webdriver
from Pages.PageElements.BasePageElements import BasePageElements
from Pages.PagesObjects.locatormethods import LocatorCommonMethods


class BasePage(LocatorCommonMethods):
    base_url = "https://www.amazon.in/"

    def __init__(self, driver: webdriver, page_url: str):
        # Load drivers
        self.driver = driver
        url = self.base_url
        # adding page url and open browser with page url
        if page_url:
            url = self.base_url + page_url
        self.driver.get(url)

        # Access Base Page Element
        self.base_page_element = BasePageElements(self.driver)


