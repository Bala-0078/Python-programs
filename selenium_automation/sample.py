from selenium import webdriver
from selenium.webdriver.common.by import By

#To prevent automatic closing of browser
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

#loads chrome compatible driver
driver=webdriver.Chrome(options=chrome_options)
#driver.get("https://www.amazon.com/instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1")
driver.get("https://www.python.org")

#price_dollar=driver.find_element(By.CLASS_NAME,value="a-price-whole")
#price_cent=driver.find_element(By.CLASS_NAME,value="a-price-fraction")
#print(f"{price_dollar.text}{price_cent.text}")

#search_bar=driver.find_element(By.NAME,value="q")
#print(search_bar.get_attribute("placeholder"))

#donate=driver.find_element(By.XPATH,value='//*[@id="touchnav-wrapper"]/header/div/div[2]/a')
#print(donate)

upcoming_event_time=driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_name=driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
event_dict={}
for i in range(len(upcoming_event_time)):
    event_dict[0]={
        "time":upcoming_event_time[i].text,
        "event_name":event_name[i].text
    }
print(event_dict)



#driver.close()
#driver.quit()