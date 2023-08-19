from bs4 import BeautifulSoup
import requests

url = "https://example.com" 

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    scripts = soup.find_all('script')
    
    for script in scripts:
        if script.get('src'):
            print(script['src'])
        else:
            print("No src attribute found for script:", script)
else:
    print("Error:", response.status_code)
