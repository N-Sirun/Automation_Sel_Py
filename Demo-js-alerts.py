import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Demoalert():
    def demo_alertbox(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")

        # Accept alert
        # driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        # time.sleep(3)
        # driver.switch_to.alert.accept()
        # time.sleep(3)

        # Dismiss alert
        # driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        # time.sleep(3)
        # driver.switch_to.alert.dismiss()
        # time.sleep(3)

        # Send text in alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(3)
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.send_keys("Nana")
        driver.switch_to.alert.accept()
        time.sleep(3)


dalert = Demoalert()
dalert.demo_alertbox()