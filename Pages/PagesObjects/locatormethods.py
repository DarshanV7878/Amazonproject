from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LocatorCommonMethods:
    def __init__(self,driver):
        self.driver = driver

    def wait_for_visibility_of_element(self, locator):
        time_to_wait = 10
        element = WebDriverWait(self.driver, time_to_wait).until(EC.presence_of_element_located(locator=locator))
        return element

    def wait_for_visibility_of_elements(self, locator):
        time_to_wait = 10
        element = WebDriverWait(self.driver, time_to_wait).until(EC.presence_of_all_elements_located(locator=locator))
        return element
