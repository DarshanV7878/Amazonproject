from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from Pages.PageElements.BasePageElements import BasePageElements


class HomePageElements(BasePageElements):
    def __init__(self, driver):
        self.driver = driver

    def get_search_bar_element(self) -> WebElement:
        return self.wait_for_visibility_of_element((By.XPATH, '//input[@id = "twotabsearchtextbox"]'))

    def get_search_button_element(self) -> WebElement:
        return self.wait_for_visibility_of_element((By.XPATH, '//input[@id = "nav-search-submit-button"]'))

    def get_results_info(self) -> WebElement:
        return self.wait_for_visibility_of_element((By.XPATH, '//span[@data-component-type="s-result-info-bar"]'))

    def get_no_result_message(self) -> WebElement:
        return self.wait_for_visibility_of_element((By.XPATH, '//span[contains(text(), "No results for ")]'))

    def get_fourth_product_from_results(self) -> WebElement:
        return self.wait_for_visibility_of_element((By.XPATH, '//span[@data-component-type="s-search-results"]'
                                                              '//div[@data-csa-c-pos= "4"]'))

    def get_add_to_cart_button(self) -> WebElement:
        return self.wait_for_visibility_of_element((By.XPATH, '//span[@data-component-type="s-search-results"]'
                                                              '//div[@data-csa-c-pos= "4"]//button[contains(text(),'
                                                              ' "Add to cart")]'))
