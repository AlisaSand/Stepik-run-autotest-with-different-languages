import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestItems:
    def test_items(self, browser):
        browser.get(URL)
        add_to_cart_button = WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//*[@id='add_to_basket_form']/button")))
        assert add_to_cart_button.is_displayed() is True, 'There is no add to cart button'


if __name__ == "__main__":

    pytest.main()
