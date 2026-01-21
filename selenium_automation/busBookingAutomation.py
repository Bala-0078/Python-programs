import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.abhibus.com/"
driver.get(url)

# Wait for elements to be interactable
wait = WebDriverWait(driver, 10)

# 1. Handle "Leaving From"
leave = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-from"]/div[1]/div/div/div/div[2]/input')))
leave.click() # Focus the field
leave.send_keys(Keys.CONTROL + "a") # Select all text
leave.send_keys(Keys.BACKSPACE)    # Delete existing (Hyderabad)
leave.send_keys("Chennai")
time.sleep(1) # Give the dropdown 1 second to appear
leave.send_keys(Keys.ENTER)

# 2. Handle "Going To"
go = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-to"]/div/div/div/div/div[2]/input')))
go.click()
go.send_keys(Keys.CONTROL + "a")
go.send_keys(Keys.BACKSPACE)
go.send_keys("Salem")
time.sleep(1)
go.send_keys(Keys.ENTER)

# 3. Handle Date (Based on your previous query)
# If the date is still wrong, you'd insert the JavaScript date change here.

# 4. Click Search
search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-button"]/a/span[2]')))
search.click()