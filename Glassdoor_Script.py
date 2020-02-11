import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

## Bringing CSV company names into `company_list`
company_list = []
errored_out_companies = []

company_urls = []

with open('Glassdoor_Companies.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    row_num = 0
    for row in csv_reader:
        if row_num == 0:
            row_num += 1
        else:
            company_list += [row[0]]

## Creating Selenium Driver
driver = webdriver.Chrome()
driver.get('https://www.glassdoor.com/profile/login_input.htm?userOriginHook=HEADER_SIGNIN_LINK')

## Logging into Glassdoor
username = "tushnae@gmail.com"
password = "SuFar6971"
driver.find_element_by_id("userEmail").send_keys(username)
driver.find_element_by_id ("userPassword").send_keys(password)
driver.find_element_by_xpath ('''//*[@id="InlineLoginModule"]/div/div/div/div/div[3]/form/div[3]/div[1]/button''').click()

for x in range(6):
    company_name = company_list[x]

    try:
        driver.get('https://www.glassdoor.com/Reviews/index.htm')
        driver.find_element_by_xpath('''//*[@id="KeywordSearch"]''').send_keys(company_name)
        driver.find_element_by_xpath ('''//*[@id="HeroSearchButton"]''').click()
        url = driver.current_url

        if "Overview" in url:   ## it has gone directly to the company page
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '''//*[@id="EIProductHeaders"]/div/a[1]'''))).click()
            
            company_urls.append((company_name,url))
            # print(company_name)
            # print(url)

        else:

            # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '''/html/body/div[3]/div/div/div/div[1]/div/div[1]/article/div[1]/div[2]/div[2]/a[1]'''))).click()

            driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div/div[1]/article/div[1]/div[2]/div[2]/a[1]").click()
            
            company_urls.append((company_name,url))


            # print(company_name)
            # print(url)
    
    except NoSuchElementException:
        errored_out_companies.append(company_name)
        continue

print(company_urls)
print(errored_out_companies)