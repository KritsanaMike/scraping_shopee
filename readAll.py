import requests

# URL of the Shopee page you want to scrape
url = 'https://shopee.co.th/-%E0%B8%AA%E0%B9%81%E0%B8%95%E0%B8%99%E0%B9%82%E0%B8%8A%E0%B8%A7%E0%B9%8C%E0%B9%81%E0%B8%99%E0%B8%A7%E0%B8%99%E0%B8%AD%E0%B8%99-%E0%B8%95%E0%B8%B0%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%87%E0%B9%82%E0%B8%8A%E0%B8%A7%E0%B9%8C%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%94%E0%B8%B1%E0%B8%9A-%E0%B8%95%E0%B8%B0%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%87%E0%B8%A5%E0%B8%A7%E0%B8%94%E0%B9%80%E0%B8%AB%E0%B8%A5%E0%B9%87%E0%B8%81-%E0%B8%AA%E0%B9%81%E0%B8%95%E0%B8%99%E0%B9%82%E0%B8%8A%E0%B8%A7%E0%B9%8C%E0%B8%AA%E0%B8%B4%E0%B8%99%E0%B8%84%E0%B9%89%E0%B8%B2-i.448625.16885083091?xptdk=aba40332-f538-487b-bb1d-8bf741e1b5a9'

# Send a GET request to fetch the raw HTML content
response = requests.get(url)
response.raise_for_status()  # Check for request errors

# Display the entire page source
print(response.text)
