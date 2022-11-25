import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Demoiframe():
    def demo_iframe(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.implicitly_wait(6)
        driver.maximize_window()
        # Switch to frame by iframe locator
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
        # Switch to frame by Index
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH, "//a[@id='navbtn_menu']").click()

        # Switch to frame by ID
        #driver.switch_to.frame("iframeResult")
        # Switch to frame by Name
        # driver.switch_to.frame("iframeResult")


diframe = Demoiframe()
diframe.demo_iframe()