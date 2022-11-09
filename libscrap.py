import requests
from bs4 import BeautifulSoup
headers = {
    'authority': 'backend.ketabonline.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'api-key': 'chf3T5y9o1YXftncU5pd45QZx9NjkJg',
    'api-lang': 'ar',
    'origin': 'https://ketabonline.com',
    'referer': 'https://ketabonline.com/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
def get_text(page):
    try:
        url = f'https://backend.ketabonline.com/api/v2/books/9632/pages/{page}'
        response = requests.get(url, headers=headers)
        content = response.json()['content']
        soup = BeautifulSoup(content, 'html.parser')
        text  = soup.get_text()
    # save the text
        with open(f'page_{page}.txt', 'w', encoding='utf-8') as f:
          f.write(text)
        return text
    except:
        print(f'Error in page {page}')
        return ''


get_text(10)