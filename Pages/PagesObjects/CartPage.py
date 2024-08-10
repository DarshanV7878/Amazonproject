from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select

from Pages.PageElements.CartPageElements import CartPageElements
from Pages.PagesObjects.BasePage import BasePage
import logging

LOG = logging.getLogger(__name__)


class CartPage(BasePage):
    page_url = "gp/cart/view.html"

    def __init__(self, driver):
        super().__init__(driver, page_url=self.page_url)
        self.cart_page_elements = CartPageElements(self.driver)

    def check_cart_product(self):
        self.cart_page_elements.get_cart_page_products().get_attribute('innerText')

    def select_quantity_of_product(self, select_quantity: int):
        select = Select(self.cart_page_elements.get_quantity_dropdown_box())
        select.select_by_value(f"{select_quantity}")

    def remove_product_from_cart(self):
        if self.cart_page_elements.get_cart_page_products().is_enabled():
            self.cart_page_elements.get_delete_button().click()
        else:
            LOG.error("Delete button is not clickable")

    def check_cart_is_empty(self):
        self.cart_page_elements.get_empty_cart_text().is_displayed()

    def check_subtotal_price(self):
        return self.cart_page_elements.get_total_price_products().text.split(".")[0].replace(",", "")

