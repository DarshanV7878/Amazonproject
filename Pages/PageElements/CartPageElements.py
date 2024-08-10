from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from Pages.PageElements.BasePageElements import BasePageElements


class CartPageElements(BasePageElements):
    def __init__(self, driver):
        self.driver = driver

    def get_cart_page_products(self) -> WebElement:
        return self.wait_for_visibility_of_element((By.ID, "sc-active-cart"))

    def get_cart_products(self) -> list:
        return  self.wait_for_visibility_of_elements((By.XPATH, '//div[ @data-itemtype="active"]'))

    def get_total_price_products(self) -> WebElement:
        return self.wait_for_visibility_of_element((By.ID, "sc-subtotal-amount-activecart"))

    def get_quantity_dropdown_box(self) -> WebElement:
        return self.wait_for_visibility_of_element((By.XPATH, '//select[@id="quantity"]'))

    def get_delete_button(self) -> WebElement:
        return self.wait_for_visibility_of_element((By.XPATH, '//input[@value="Delete"]'))

    def get_empty_cart_text(self) -> WebElement:
        return self.wait_for_visibility_of_element(
            (By.XPATH, '//h1[contains(text(), "Your Amazon Cart is empty.")]'))
