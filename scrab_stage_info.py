import requests
from bs4 import BeautifulSoup

# 目標網頁的URL
url = "https://tos.fandom.com/zh/wiki/%E6%94%B9%E9%9D%A9%E7%9A%84%E9%96%8B%E7%AB%AF"

# 發送HTTP請求並獲取網頁內容
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup解析HTML內容
soup = BeautifulSoup(html_content, 'html.parser')

# 找到目標表格的<tbody>標籤
table_body = soup.find('tbody')

# 顯示<tbody>標籤的內容
print(table_body)
