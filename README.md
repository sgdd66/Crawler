# Crawler

## 引言
这个库主要存储我在学习网络爬虫技术的练习代码

## BeautifulSoup学习笔记
### BeautifulSoup基本元素
>Tag:标签
>Name:标签名
>Attributes:标签属性
>NavigableString:标签内非属性字符串
>Comment:标签注释

### BeautifulSoup遍历方法
1.标签树的下行遍历
>.contents   子节点的列表，将\<Tag>所有儿子节点存入列表
>.children    子节点的迭代类型，与.contents类似，用于循环遍历儿子节点
>.descendants   子孙节点的迭代类型，包含所有自损节点，用于循环遍历

2.上行遍历
>.parent   返回节点的父亲标签
>.parent   返回节点的先辈节点

3.平行遍历 （发生在同一个父亲节点下的各个节点间）
>.next_sibling   返回按照HTML文本顺序的下一个平行节点标签
>.previous_sibling   返回按照HTML文本顺序的上一个平行节点标签
>.next_siblings   返回按照HTML文本顺序的后续所有平行节点标签
>.previous_siblings   返回按照HTML文本顺序的前序所有平行节点标签

## 正则表达式
练习使用re库的六种操作，最后练习使用正则表达式爬取淘宝网站中的信息

## scrapy
练习使用scrapy库，并使用其爬取股票交易信息
