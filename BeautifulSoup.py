"""这段代码用于测试beautiful soup的功能"""

from bs4 import BeautifulSoup

soup=BeautifulSoup("<p>data</p>","html.parser")
print(soup.prettify())