from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Chrome()
browser.get('https://food.ru/kalkulyator-kalorii')

buttonAge = browser.find_element(By.NAME, "age")

buttonAge.send_keys('25')

buttonH=browser.find_element(By.NAME, "height")
buttonH.send_keys('175')
buttonW=browser.find_element(By.NAME, "weight")
buttonW.clear()
buttonW.send_keys('65')
#buttonR.click()
button=browser.find_element(by=By.CSS_SELECTOR, value='._18Bed')

button.click()


try:
    assert 'Калькулятор расчёта калорий' in browser.title
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')

try:
    assert 'результат' in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')

browser.close()



