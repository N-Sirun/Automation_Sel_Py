from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('C:/Users/Narine_Sirunyan/Desktop/Exercise Files/Source Code/chromedriver')
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
driver.implicitly_wait(6)
source = driver.find_element_by_xpath('//*[@id="box7"]')
dest = driver.find_element_by_xpath('//*[@id="box107"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, dest).perform()
