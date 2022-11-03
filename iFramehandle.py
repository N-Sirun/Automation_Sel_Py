import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Demoiframe():
    def demo_iframe(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH, "//a[@id='navbtn_menu']").click()
        time.sleep(4)


diframe = Demoiframe()
diframe.demo_iframe()