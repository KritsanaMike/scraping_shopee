from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
# Path to your ChromeDriver
chrome_driver_path = 'C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'

# Set up the WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the Shopee page
url = 'https://shopee.co.th/-%E0%B8%AA%E0%B9%81%E0%B8%95%E0%B8%99%E0%B9%82%E0%B8%8A%E0%B8%A7%E0%B9%8C%E0%B9%81%E0%B8%99%E0%B8%A7%E0%B8%99%E0%B8%AD%E0%B8%99-%E0%B8%95%E0%B8%B0%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%87%E0%B9%82%E0%B8%8A%E0%B8%A7%E0%B9%8C%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%94%E0%B8%B1%E0%B8%9A-%E0%B8%95%E0%B8%B0%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%87%E0%B8%A5%E0%B8%A7%E0%B8%94%E0%B9%80%E0%B8%AB%E0%B8%A5%E0%B9%87%E0%B8%81-%E0%B8%AA%E0%B9%81%E0%B8%95%E0%B8%99%E0%B9%82%E0%B8%8A%E0%B8%A7%E0%B9%8C%E0%B8%AA%E0%B8%B4%E0%B8%99%E0%B8%84%E0%B9%89%E0%B8%B2-i.448625.16885083091?xptdk=aba40332-f538-487b-bb1d-8bf741e1b5a9'
driver.get(url)

# Wait for the page to load dynamically
driver.implicitly_wait(10)  # Adjust time as needed


style_element = driver.find_element(By.CSS_SELECTOR, 'script[type="text/mfe-initial-data"]')
style_content = style_element.get_attribute('innerHTML')

# Print or process the data
# print(style_content)
try:
    data = json.loads(style_content)
    # Pretty-print the JSON data
    pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
    print(pretty_json)
except json.JSONDecodeError:
    print("Failed to decode JSON. The script content may not be valid JSON.")

# Close the WebDriver
driver.quit()









# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import json

# # Path to your ChromeDriver
# chrome_driver_path = 'C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'

# # Path to your Chrome user data directory
# user_data_dir = 'C:/Users/User/AppData/Local/Google/Chrome/User Data/'

# # Specify the profile directory (in your case, Profile 14)
# profile_directory = 'Profile 3'

# # Set up Chrome options
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
# chrome_options.add_argument(f'--profile-directory={profile_directory}')

# # Set up the WebDriver with Chrome options
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Open the Shopee page
# url = 'https://shopee.co.th/-%E0%B8%AA%E0%B9%81%E0%B8%95%E0%B8%99%E0%B9%82%E0%B8%8A%E0%B8%A7%E0%B9%8C%E0%B9%81%E0%B8%99%E0%B8%A7%E0%B8%99%E0%B8%AD%E0%B8%99-%E0%B8%95%E0%B8%B0%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%87%E0%B9%82%E0%B8%8A%E0%B8%A7%E0%B9%8C%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%94%E0%B8%B1%E0%B8%9A-%E0%B8%95%E0%B8%B0%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%87%E0%B8%A5%E0%B8%A7%E0%B8%94%E0%B9%80%E0%B8%AB%E0%B8%A5%E0%B9%87%E0%B8%81-%E0%B8%AA%E0%B9%81%E0%B8%95%E0%B8%99%E0%B9%82%E0%B8%8A%E0%B8%A7%E0%B9%8C%E0%B8%AA%E0%B8%B4%E0%B8%99%E0%B8%84%E0%B9%89%E0%B8%B2-i.448625.16885083091?xptdk=aba40332-f538-487b-bb1d-8bf741e1b5a9'
# driver.get(url)

# # Wait for the page to load dynamically
# driver.implicitly_wait(10)  # Adjust time as needed

# style_element = driver.find_element(By.CSS_SELECTOR, 'script[type="text/mfe-initial-data"]')
# style_content = style_element.get_attribute('innerHTML')

# # Print or process the data
# try:
#     data = json.loads(style_content)
#     # Pretty-print the JSON data
#     pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
#     print(pretty_json)
# except json.JSONDecodeError:
#     print("Failed to decode JSON. The script content may not be valid JSON.")

# # Close the WebDriver
# driver.quit()


