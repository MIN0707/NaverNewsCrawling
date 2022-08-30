import requests
from bs4 import BeautifulSoup
import time
import os
import pandas as pd

url = 'https://sports.news.naver.com/index'
response = requests.get(url)
dom = BeautifulSoup(response.text, 'html.parser')
element = dom.select('.today_item .title')
result = []
for ele in element:
    result.append(ele.text.strip())


now = time.strftime("%Y.%m.%d %H %M %S")
# print(now)

fileName = f'네이버 스포츠 뉴스 {now}.csv'
# print(fileName)

filePath = os.path.join(os.getcwd(), 'out', fileName)

path = 'out'
if not os.path.exists(path):
    os.mkdir(path)
    print(f'{path} 경로가 생성되었습니다')
else:
    print(f'{path} 경로가 이미 있습니다.')

df = pd.DataFrame([], columns=['뉴스'])

for title in result:
    df.loc[len(df)] = title

df.to_csv(filePath, encoding='euc-kr')

# with open(filePath, 'w', encoding="utf-8") as f:
#     for title in result:
#         f.write(title + '\n')
