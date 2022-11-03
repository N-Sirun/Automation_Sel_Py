import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class Demodragndrop():
    def demo_dragndrop(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        dragelem = driver.find_element(By.XPATH, "//div[@id='draggable']")
        dropelem = driver.find_element(By.XPATH, "//div[@id='droppable']")
        #ActionChains(driver).drag_and_drop(dragelem, dropelem).perform()\
        ActionChains(driver).drag_and_drop_by_offset(dragelem, 50, 30).perform()
        time.sleep(3)


ddrag = Demodragndrop()
ddrag.demo_dragndrop()