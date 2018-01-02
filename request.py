import requests
import os

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "error occur"

def getHTMLHeader(url):
    try:
        r=requests.head(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.headers
    except:
        return "error occur"

#爬取京东的商品信息
def JDinfo():
    """爬取京东的商品信息"""
    url="https://item.jd.com/2967929.html"
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return "error occur"

#爬取亚马逊的商品信息
def amazonInfo():
    """爬取亚马逊的商品信息"""
    url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
    try:
        kv={'user-agent':'Mozilla/5.0'}
        r = requests.get(url, timeout=30,headers=kv)
        if(r.status_code!=200):
            print(r.status_code)
            return
        print(r.request.headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return "error occur"

#依靠关键字爬取百度的信息
def baiduInfo():
    """依靠关键字爬取百度的信息"""
    kv={'wd':'python'}
    r=requests.get("http://www.baidu.com/s",params=kv)
    print(r.request.url)
    print(len(r.text))

#爬取360的信息
def q360Info():
    """爬取360的信息"""
    kv={'q':'python'}
    r=requests.get("http://www.so.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))

# 网络图片爬取
def jpgSave():
    url = "http://v.youku.com/v_show/id_XMzI3MzAyMDg3Ng"
    root='E:/pic//'
    path=root+url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r=requests.get(url)
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print("succeed:{0}".format(r.status_code))
        else:
            print("file has existed")
    except:
        print('error occur')


if __name__=="__main__":
    jpgSave()
