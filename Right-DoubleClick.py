import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class Democlicks():
    def demo_click(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        driver.implicitly_wait(6)
        # Right Click
        achains = ActionChains(driver)
        elem1 = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        achains.context_click(elem1).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Delete']").click()
        driver.switch_to.alert.accept()

        # Double click
        bchains = ActionChains(driver)
        elem2 = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        bchains.double_click(elem2).perform()
        driver.switch_to.alert.accept()



dclick = Democlicks()
dclick.demo_click()