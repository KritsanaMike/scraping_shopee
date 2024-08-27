from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Specify the URL of the Shopee page you want to scrape
url = "https://shopee.co.th/search?keyword=%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%94%E0%B8%88%E0%B8%AD%20nvidia&trackingId=searchhint-1709273327-2a6ad59a-d792-11ee-8a58-d6d739c1bc99"

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get(url)
    
    # Wait for the page to load (you can adjust the sleep time as needed)
    time.sleep(5)

    # Extract data from the page
    total_items_element = driver.find_element(By.CLASS_NAME, "shopee-mini-page-controller__total")
    total_items = total_items_element.text.strip()  # Extract text and remove leading/trailing whitespace
    
    # Print the total number of items
    print("Total Items:", total_items)
    
finally:
    # Close the browser window
    driver.quit()
