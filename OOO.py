# -*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
# driver.get("https://ope.yiwise.com")
# sleep(0.5)
# driver.find_element_by_xpath('//*[@id="app"]/div/form[2]/div[2]/div/div/input').send_keys("18438615273")
# sleep(1)
# driver.find_element_by_xpath('//*[@id="app"]/div/form[2]/div[3]/div/div/input').send_keys("Liu123")
# sleep(1)
# driver.find_element_by_xpath('//span[text()="登录"]')
# sleep(0.5)
# element = driver.find_element_by_xpath('//*[@id="pane-directCustomer"]/div/div[1]/div[1]/div/div/div[1]/span/span/i')
# action = ActionChains(driver)
# action.click(element)
driver.get('https://www.baidu.com')
actions = ActionChains(driver)
actions.move_to_element(driver.find_element_by_xpath('//*[@id="s-top-left"]/div/a')).perform()
