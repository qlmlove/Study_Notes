# Selenium 以“篇”概全

## 一、安装selenium包

1. 安装最新版： `pip install selenium`
2. 安装旧版本：`pip install selenium==`



## 二、导包

```python
# 常用的
from selenium import webdriver

# 导入按键
from selenium.webdriver.common.keys import Keys

# 用于select下拉列表控件
from selenium.webdriver.support.select import Select
```

## 三、驱动

可以直接去 [Nuget](https://www.nuget.org/packages?q=Tags%3A%22WebDriver%22) 或者 [PyPI::Selenium](https://pypi.org/project/selenium/#drivers) 列出的位置按需要寻找，也可以直接在下边列出的网站下载

### Chrome

1. [淘宝镜像下载](http://npm.taobao.org/mirrors/chromedriver/) 
2. [chrome官网下载](http://chromedriver.storage.googleapis.com/index.html)
3. https://www.nuget.org/packages/Selenium.WebDriver.ChromeDriver/
4. 

### Firefox

1. https://github.com/mozilla/geckodriver/releases
2. https://www.nuget.org/packages/Selenium.WebDriver.GeckoDriver/

### IE

1. https://www.nuget.org/packages/Selenium.WebDriver.IEDriver/





**注意：**

1. **`chromedriver.exe`文件必须位于path配置的环境变量中**
2. **可以不与python或chrome同处于一个文件夹**，比如我就放在 `C:\soft` 文件夹中

## webdriver配置

略

## driver常用方法和属性（以Chrome为例）

```python
from selenium import webdriver

# 打开Chrome
driver = webdriver.Chrome()

# 打开指定网址
driver.get('http://www.baidu.com')

 #关闭当前标签页，Chrome默认关闭最后一个标签页会退出Chrome，但是chromedriver还在后台运行
driver.close()

#关闭浏览器并退出chromedriver
driver.quit()

# 获取当前页面标题属性
driver.title

# 获取当前浏览器名字
driver.name # 输出： 'chrome'

# 输出当前URL
driver.current_url

# 获取当前页面元素 
driver.page_source

# 回退到之前打开的页面 
driver.back()

# 前进到回退之前的页面 
driver.forward()

# 页面刷新 
driver.refresh()

# 截取当前页面并保存到1.png  
driver.get_screenshot_as_file("./1.png") # 成功则返回True

# 设置浏览器窗口大小：
driver.set_window_size(800,600)

# 最小化
driver.minimize_window()

# 最大化
driver.maximize_window()
```



## 元素定位

### id

```python

```

