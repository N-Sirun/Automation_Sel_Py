import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Demodisplayed():
    def demo_displayed(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem)
        driver.implicitly_wait(6)
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        elem1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem1)

displayed = Demodisplayed()
displayed.demo_displayed()
