from selenium.common import NoSuchElementException

from Pages.PageElements.HomePageElements import HomePageElements
from Pages.PagesObjects.BasePage import BasePage
import logging

LOG = logging.getLogger(__name__)


class HomePage(BasePage):
    page_url = ""

    def __init__(self,driver):
        super().__init__(driver, page_url=self.page_url)
        self.home_page_elements = HomePageElements(self.driver)

    def search_item(self, item_name: str):
        self.home_page_elements.get_search_bar_element().send_keys(item_name)
        self.home_page_elements.get_search_button_element().click()

    def add_to_cart_fourth_product(self):
        fourth_product_text = self.home_page_elements.get_fourth_product_from_results().text

        if "Add to cart" in fourth_product_text:
            self.home_page_elements.get_add_to_cart_button().click()
            LOG.info("clicked on add to cart button")
        else:
            raise NoSuchElementException
















