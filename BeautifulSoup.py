"""这段代码用于测试beautiful soup的功能"""

from bs4 import BeautifulSoup
import bs4
import requests

#安装测试函数
def test1():
    #BeautifulSoup 支持的解析器有'html.parser', 'lxml', 'xml', 'html5lib'
    soup=BeautifulSoup("<p>data</p>","html.parser")
    print(soup.prettify())

#获取测试数据
def load_data():
    url='http://python123.io/ws/demo.html'
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        str="error in open url:{0}".format(url)
        print(str)
        return str

#标签内容提取
def test2():
    soup = BeautifulSoup(load_data(),'html.parser')
    #a是html中的一个标签
    tag = soup.a
    #tag是代表整个标签的内容
    print(type(tag),'   ',tag)
    #tag.string代表标签之间的内容
    print(type(tag.string),'    ',tag.string)
    #NavigableString可以和string变量互操作
    if tag.string=='Basic Python':
        print("ssss")

#标签属性提取
def test3():
    soup = BeautifulSoup(load_data(),'html.parser')
    tag = soup.a
    #attrs contain all attribute of the tag
    print(tag.attrs)
    #attrs is a dict variable, you can use key to look for value
    print(tag.attrs['id'])

#注释与内容的区别
def test4():
    soup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", 'html.parser')
    tag_b=soup.b
    tag_p= soup.p
    print("{0}   {1}".format(type(tag_b.string),tag_b.string))
    print("{0}   {1}".format(type(tag_p.string),tag_p.string))

#遍历网页中的内容
def test5():
    soup = BeautifulSoup(load_data(),'html.parser')

    #下行遍历
    tag = soup.body
    print(tag.contents)
    for child in tag.children:
        print(child)

    #上行遍历
    tag = soup.a
    for parent in tag.parents:
        if parent is None:
            print(parent)
        else:
            print(parent.name)

    #平行遍历
    tag = soup.p
    for next_sibling in tag.next_siblings:
        print(next_sibling)

#提取链接信息
def test6():
    soup = BeautifulSoup(load_data(),'html.parser')
    for link in soup.find_all('a'):
        #这两种方法是等价的
        print(link.get('href'))
        #print(link.attrs['href'])

#中国大学排名
class test7(object):

    def __init__(self):
        self.getInfo()
        self.printInfo()

    def getWebText(self):
        url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
        try:
            kv = {'user-agent': 'Mozilla/5.0'}
            r = requests.get(url, timeout=30, headers=kv)
            r.raise_for_status()
            r.encoding=r.apparent_encoding
            return r.text
        except:
            print('error in open url:{0}'.format(url))

    def getInfo(self):
        html = self.getWebText()
        soup = BeautifulSoup(html,'html.parser')
        self.info=[]
        for tr in soup.find('tbody').children:
            if isinstance(tr,bs4.element.Tag):
                tds = tr.find_all('td')
                self.info.append([tds[0].string,tds[1].string,tds[3].string])

    def printInfo(self):
        # print("{:^10}\t{:^6}\t{:^10}".format("排名", "大学", "成绩"))
        # for i in range(50):
        #     u = self.info[i]
        #     print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))

        tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
        print(tplt.format("排名", "学校名称", "总分", chr(12288)))
        for i in range(50):
            u = self.info[i]
            print(tplt.format(u[0], u[1], u[2], chr(12288)))






if __name__=='__main__':
    t=test7()