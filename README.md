# Python 网络爬虫专题分享

## 一、什么是网络爬虫

### 概念
> 网络爬虫，是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。

### 功能模块组成
1. 控制器：启动进程/线程对相关URL发起网络请求。
2. 解析器：下载网页、对网页文本进行过滤解析
3. 数据持久化：将解析得到爬虫数据保存。

### 一个简单的爬虫
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
```

## 二、Python网络爬虫常用库

### 网络请求
1. urlopen：主要用于发送get请求，获取资源
2. requests：可发送POST等请求，用于表单处理等

### HMTL解析
BeautifulSoup4

### JavaScript解析
selenium

### 图像识别与文字处理
1. numpy
2. Pillow
3. Tesseract

## 三、爬虫的方式

1. 直接爬取HTML解析

2. 抓取JavaScript解析
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path='drivers/chromedriver',
    options=chrome_options)

driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
try:
    element = WebDriverWait(driver, 10).until(
                       EC.presence_of_element_located((By.ID, 'loadedButton')))
finally:
    print(driver.find_element_by_id('content').text)
    driver.close()
```

3. 利用API抓取

## 四、数据存储
1. 媒体文件：如jpg、mp3、mp4等媒体文件
2. 数据存储到txt、csv等文本文件
可使用python等csv库等
3. 数据存储到MySQL数据库

## 五、爬虫的延伸

### 表单处理及登陆验证
1. 使用requests模拟表单提交
```python
import requests

params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post("http://pythonscraping.com/pages/processing.php", data=params)
print(r.text)
```

2. 验证码处理
借助Tesseract、Pillow等OCR库识别验证码。

### Python爬虫框架Scrapy

#### 框架简介

> Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。

#### 安装方式
1. Anaconda安装
```shell
conda install -c conda-forge scrapy
```
2. pip安装
```powershell
pip3 install scrapy
```
#### 创建项目
```
1. scrapy startproject 项目名称
```

```
2. cd project_name（进入项目目录）
```

```
3. scrapy genspider 应用名称 爬取网页的起始url 
（例如：scrapy genspider douban_book_spider https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T>）
执行完毕后，会在项目的spiders中生成一个应用名的py爬虫文件：应用名.py
```

#### 项目结构解析

```
project_name/
   scrapy.cfg          #项目的主配置信息。
   project_name/
       __init__.py
       items.py        #设置数据存储模板，用于结构化数据，如：Django的Model
       pipelines.py    #数据持久化处理
       settings.py     #配置文件，如：递归的层数、并发数，延迟下载等
       spiders/        #爬虫目录，如：创建文件，编写爬虫解析规则
           __init__.py
```

## 六、爬虫实例
#### 基于Python原生库的豆瓣图书爬虫
详见爬虫脚本代码：[/douban_book_spider/DoubanSpider.py](https://github.com/uniquetree/python-study-spiders/tree/master/douban_book_spider/DoubanSpider.py)

#### 基于爬虫框架Scrapy的豆瓣图书爬虫
详见项目：[simple_scrapy](https://github.com/uniquetree/python-study-spiders/tree/master/simple_scrapy/simple_scrapy/spiders/douban_book_spider.py)

## 七、项目Github地址
[https://github.com/uniquetree/python-study-spiders](https://github.com/uniquetree/python-study-spiders)

## 八、推荐书籍
> 《Python网络爬虫权威指南》

