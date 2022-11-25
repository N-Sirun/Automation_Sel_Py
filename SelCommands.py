import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoLearnSel():
    def demobrowsermethods(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://trinket.io/python3")
        driver.implicitly_wait(6)
        driver.maximize_window()
        driver.implicitly_wait(6)
        driver.fullscreen_window()
        driver.refresh()
        driver.find_element(By.LINK_TEXT, "Learn More »")
        driver.back()
        driver.forward()
        driver.minimize_window()
        driver.maximize_window()
        driver.quit()

demobrowser = DemoLearnSel()
demobrowser.demobrowsermethods()