import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

## Bringing CSV company names into `company_list`
company_list = []
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

## Testing one company in glassdoor search
company_name = company_list[0]
# driver.find_element_by_xpath("//*[@id='sc.keyword']").send_keys(company_name)
            # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sc.keyword']")))

WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, "sc.keyword"))).send_keys(company_name)
# dropdownSelect = Select(driver.find_element_by_xpath('''//*[@id="SiteSrchTop"]/form/div/ul'''))

driver.find_element_by_xpath('''//*[@id="SiteSrchTop"]/form/div/ul/li[2]''').click()

# dropdownSelect.select_by_index(0).click()


driver.find_element_by_id("HeroSearchButton").click()


# driver.find_element_b
# python_button = driver.find_elements_by_id()



# driver.find_element_by_id(“submit”).click()





