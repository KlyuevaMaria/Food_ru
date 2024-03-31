from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Chrome()
browser.get('https://food.ru/')

buttonFilter=browser.find_element(by=By.CSS_SELECTOR, value='.searchInput_filtersButton__3Rk7A')
buttonFilter.click()

buttonArticle=browser.find_element(by=By.CSS_SELECTOR, value='.tag_tag__BBDqQ')
buttonArticle.click()

try:
    assert 'статья' in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')

browser.close()

