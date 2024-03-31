from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Chrome()
browser.get('https://food.ru/')
search=browser.find_element(by=By.CSS_SELECTOR, value='.searchInput_input__pL2xy')
search.send_keys('Чёрный лес')

button=browser.find_element(by=By.CSS_SELECTOR, value='.searchInput_submitButton__nf3o_')
button.click()

try:
    assert 'Чёрный лес' in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')

browser.close()

