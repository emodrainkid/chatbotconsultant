import pprint
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://n-katalog.ru/")
s = []
time.sleep(3)
catalog_elements = driver.find_element(By.ID, 'main-menu').find_elements(By.CLASS_NAME, "trend__item")
for i in catalog_elements[1:]:
    time.sleep(1)
    driver.get(i.find_element(By.XPATH, 'a').get_attribute('href'))
    submit_button = driver.find_elements(by=By.CLASS_NAME, value="model-short-info")
    for j in range(5):
        s.append(submit_button[j].text)
    print(*s)
    pass
# title_element = driver.find_element(By.TAG_NAME, 'h1')
# pprint.pprint(catalog_elements)
# print(list(catalog_element.text))
# page_title = title_element.text
# print(f"{page_title}")
driver.quit()