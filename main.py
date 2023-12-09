from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from data import my_email, my_password

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(chrome_options)


driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3778771330&f_WT=2&keywords=Python%20Developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
sleep(2)
sign_in_button=driver.find_element(By.XPATH,'/html/body/div[4]/a[1]' )
sign_in_button.click()

email_field=driver.find_element(By.ID, "username")
email_field.send_keys(my_email)

password_field=driver.find_element(By.ID, "password")
password_field.send_keys(my_password)

sign_in=driver.find_element(By.CSS_SELECTOR, "#organic-div form button")
sign_in.click()
sleep(2)
jobs=driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")
print(len(jobs))
for job in jobs:
    driver.execute_script("arguments[0].scrollIntoView();", job)
    sleep(2)
    job.click()
    sleep(3)
    save_job=driver.find_element(By.CSS_SELECTOR, '.mt5 .artdeco-button--secondary')
    save_job.click()
    print("saved")
    sleep(2)




