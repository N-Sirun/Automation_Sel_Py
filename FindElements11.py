import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindElementByLink():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://trinket.io/python3")
        driver.implicitly_wait(6)
        lista = driver.find_elements(By.TAG_NAME, "a")
        print(len(lista))
        for i in lista:
            print(i.text)


findbyid = DemoFindElementByLink()
findbyid.locate_by_id_demo()