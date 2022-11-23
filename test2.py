import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestSelenium(unittest.TestCase):

    def test_add_to_shopping_cart(self) -> None:
        """Add to shopping cart"""
        driver = webdriver.Chrome(
            executable_path='./chromedriver'
        )

        driver.get("http://tutorialsninja.com/demo/")
        search_field = driver.find_element(By.NAME, "search")
        search_field.send_keys("iphone")
        search_field.send_keys(Keys.RETURN)

        add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="content]/div[3]/div/div/div[2]/div[2]/button[1]')
        add_to_cart_button.click()
        shopping_cart_link = driver.find_element(By.LINK_TEXT, "Shopping Cart")
        shopping_cart_link.click()

        self.assertTrue("product 11" in driver.page_source)


        driver.close()