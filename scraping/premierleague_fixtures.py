"""
README
my code gets a full season premier league results and make a excel file to store them.
"""

from select import select
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

all_matches_buttom = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_buttom.click()

dropdown = Select(driver.find_element_by_id('country'))
country = 'Spain'
dropdown.select_by_visible_text(country)

time.sleep(5)


matches = driver.find_elements_by_tag_name('tr')

date = []
home_team = []
score = []
away_team = []
for match in matches:
    date.append(match.find_element_by_xpath('./td[1]').text)
    home = match.find_element_by_xpath('./td[2]').text
    #print(home)
    home_team.append(home)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)
    
driver.close()

df = pd.DataFrame({'date' : date, 'home' : home_team, 'score': score, 'away' : away_team})
df.to_excel(f'football_data_{country}.xlsx', index=False)

print(df.head())


