import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class Demoimplicit():
    def demo_waitimplicit(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://login.salesforce.com/")
        driver.implicitly_wait(6)
        driver.find_element(By.ID, "username").send_keys("N.Sirun")
        driver.find_element(By.ID, "passwo55rd").send_keys("N.Sirun22")


implwait = Demoimplicit()
implwait.demo_waitimplicit()