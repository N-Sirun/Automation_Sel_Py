import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemodropdownSelect():
    def demo_dropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/au/form/signup/freetrial-sales/")
        driver.implicitly_wait(6)
        dropdwn = driver.find_element(By.NAME, "UserTitle")
        dd = Select(dropdwn)
        dd.select_by_index(1)
        dd.select_by_visible_text("Customer Service Manager")
        dd.select_by_value("Marketing_PR_Manager_ANZ")

dropdwn_check1 = DemodropdownSelect()
dropdwn_check1.demo_dropdown()


# select. var2 = driver.find_element(By.XPATH, "//label[normalize-space()='One']//span[@class='radiobtn']").is_selected()
# print(var2)