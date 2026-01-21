from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
#url="https://en.wikipedia.org/wiki/Main_Page"
#url="https://www.wikipedia.org/"
url="https://secure-retreat-92358.herokuapp.com/"
driver.get(url)
#article_count=driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
#article_count.click()

#find search <input> by name
#search=driver.find_element(By.NAME, value="search")

#sending keyboard input to selenium
#search.send_keys("python",Keys.ENTER)

firstName=driver.find_element(By.NAME,value="fName")
lastName=driver.find_element(By.NAME,value="lName")
Email=driver.find_element(By.NAME,value="email")
button=driver.find_element(By.CSS_SELECTOR,value=".btn.btn-lg.btn-primary.btn-block")
firstname="Balamurugan"
lastname="v"
email="bala@mail.com"
firstName.send_keys(firstname)
lastName.send_keys(lastname)
Email.send_keys(email)
button.click()
