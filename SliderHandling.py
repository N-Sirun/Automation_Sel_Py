import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class Demoslider():
    def demo_sliderone(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.snapdeal.com/products/mens-footwear-casual-shoes?q=Price%3A349%2C2712%7C&sort=plrty#bcrumbLabelId:393")

        driver.implicitly_wait(6)
        driver.maximize_window()
        sliderleft = driver.find_element(By.XPATH, "//a[contains(@class, 'left-handle')]")
        sliderright = driver.find_element(By.XPATH, "//a[contains(@class, 'right-handle')]")
       # ActionChains(driver).drag_and_drop_by_offset(sliderleft, 60, 0).perform()
        ActionChains(driver).click_and_hold(sliderleft).pause(1).move_by_offset(50,0).release().perform()
        # ActionChains(driver).drag_and_drop_by_offset(sliderright, 40, 0).perform()
        ActionChains(driver).click_and_hold(sliderright).pause(1).move_by_offset(-60, 0).release().perform()


sliderdrag = Demoslider()
sliderdrag.demo_sliderone()
