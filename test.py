from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
ser = Service("./chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


driver.get("http://tutorialsninja.com/demo/")

search_field = driver.find_element(By.NAME, "search")
search_field.send_keys("iphone")
search_field.send_keys(Keys.RETURN)

add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
add_to_cart_button.click()

shopping_cart_link = driver.find_element(By.LINK_TEXT, "Shopping Cart")
shopping_cart_link.click()

assert "product 11" in driver.page_source
driver.close()

pass

