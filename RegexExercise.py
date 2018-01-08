"""正则表达式练习文件"""
import re
import requests

#search 全文搜索
def test1():
    match = re.search(r'[1-9]\d{5}',  'BIT 100081')
    if match:
        print(match.group(0))

#match 从文本开始处匹配
def test2():
    match =re.match(r'.*([1-9]\d{5})',  'BIT 100081')
    if match:
        print(match.group(0))

#findall
def test3():
    match = re.findall(r'[1-9]\d{5}', 'Bit 100084 100895')
    print(match)

#split
def test4():
    match = re.split(r'[1-9]\d{5}', 'Bit100084 ert100895')
    print(match)
    match = re.split(r'[1-9]\d{5}', 'Bit100084 ert100895',maxsplit=1)
    print(match)

#finditer
def test5():
    for m in re.finditer(r'[1-9]\d{5}', 'Bit100084 ert100895'):
        if m:
            print(m.group(0))
    print(type(re.finditer(r'[1-9]\d{5}', 'Bit100084 ert100895')))

#sub
def test6():
    match=re.sub(r'[1-9]\d{5}', ':zipcode','Bit100081 TSU100084')
    print(match)

#面向对象使用
def test7():
    regex = re.compile(r'[1-9]\d{5}')
    str = regex.search('Bit100081 TSU100084')
    print(str.group(0))
    print(str.start(),str.end(),str.span())
    print(str.string)

#贪婪匹配与懒惰匹配
def test8():
    regex_greed = re.compile(r'py.*n')
    regex_lazy = re.compile(r'py.*?n')
    demo = "pyqnwnen"
    print(regex_greed.search(demo).group(0))
    print(regex_lazy.search(demo).group(0))

#淘宝页面信息提取
class test9(object):
    def __init__(self,name):
        self.info=[]
        url_root='https://s.taobao.com/search?q=' + name
        for i in range(2):
            try:
                url = url_root+'&s='+str(44*i)
                html = self.getWebHtml(url)
                self.getInfo(html)
            except:
                print("error")
        self.printInfo()

    def getWebHtml(self,url):
        try:
            kv = {'user-agent': 'Mozilla/5.0'}
            r = requests.get(url, timeout=30, headers=kv)
            r.raise_for_status()
            r.encoding=r.apparent_encoding
            return r.text
        except:
            print("error in open url:{0}".format(url))

    def getInfo(self,html):
        try:
            titles = re.findall(r'\"raw_title\"\:\".+?\"',html)
            prices = re.findall(r'\"view_price\"\:\".+?\"',html)
            for i in range(len(titles)):
                price = eval(prices[i].split(':')[1])
                title = eval(titles[i].split(':')[1])
                self.info.append([title,price])
        except:
            print("error in getting infomation")

    def printInfo(self):
        for i in range(len(self.info)):
            print("{0}:{1}".format(self.info[i][0],self.info[i][1]))




if __name__=='__main__':
    t= test9("书包")
