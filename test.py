from selenium import webdriver   # 导入webdriver包  
  
dr = webdriver.Firefox()    # 初始化一个火狐浏览器实例：driver
#dr=webdriver.Chrome()     调用谷歌浏览器
#dr=webdriver.Ie()   #调用IE浏览器
  
dr.maximize_window()        # 最大化浏览器  
  
dr.get("http://10.5.10.59:10053/")  # 通过get()方法，打开一个url站点  
  
#dr.quit()     #关闭并退出浏览器  
