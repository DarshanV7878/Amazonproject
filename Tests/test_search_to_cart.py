import time

from Pages.PagesObjects.CartPage import CartPage
from Pages.PagesObjects.HomePage import HomePage
import logging

LOG = logging.getLogger(__name__)


def test_search_invalid_items(get_driver):
    # Step 1:Search for an no existing product (e.g., "ld345tsxslfer")
    driver = get_driver
    home_page = HomePage(driver)
    home_page.search_item("ld345tsxslfer")
    result_element = home_page.home_page_elements.get_no_result_message()
    assert "No results for" in result_element.text, "message not found after entered invalid input"


def test_valid_search_and_add_to_cart_valid_items(get_driver):
    # Step 2: Search for an existing product (e.g., "Laptop")
    driver = get_driver
    home_page = HomePage(driver)
    home_page.search_item("Laptop")
    result_element = home_page.home_page_elements.get_results_info()
    assert 'results for "Laptop"' in result_element.text, "Results for laptop not displayed"

    # Step 3: Add a product to the cart
    home_page.add_to_cart_fourth_product()
    time.sleep(5)
    cart_page = CartPage(driver)
    check_product_details = cart_page.cart_page_elements.get_cart_page_products()
    assert "Qty:1" and "Subtotal (1 item)" in check_product_details.get_attribute("innerText"), (
        "Product not added in cart")
    existing_price = cart_page.check_subtotal_price()

    # Step 4: Add a product to the cart
    quantity = 3
    cart_page.select_quantity_of_product(quantity)
    time.sleep(5)
    check_product_details = cart_page.cart_page_elements.get_cart_page_products()
    assert f"Qty:{quantity}" and f"Subtotal ({quantity} items)" in check_product_details.get_attribute("innerText"), (
        "Product is not updated in cart")
    updated_price = cart_page.check_subtotal_price()
    assert int(updated_price) == int(existing_price) * quantity, "price is not updated"

    # Step 5: Remove a product from the cart
    cart_page.remove_product_from_cart()
    cart_page.check_cart_is_empty()
    assert "Your Amazon Cart is empty." in check_product_details.get_attribute("innerText"), "Cart is not empty"
