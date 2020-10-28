from selenium import webdriver
import time

# 要爬的網頁
page = "https://sbl.choxue.com/player/_GGDTifCtrkotU3Ui0dZNg"

# driver抓下來以後放的路徑
driver = webdriver.Chrome('/Users/evanyo25/Applications/Chrome Apps.localized/chromedriver')
driver.get(page)

# 給他開啟的時間，不留點時間網頁會還沒載好，會抓不到東西
time.sleep(5)


# 用 class name 去 find elements <--s 加s表示找多個
# 回傳一個 list of element 用 for 去展開他
col = driver.find_elements_by_class_name("col-xs-6")
for i in col:
	# 每一個小 element 再次以 tag name （舉例來說：p, div, body） 來去 find elements
	a = i.find_elements_by_tag_name('p')
	for j in a:
		print(j.text) # 找到的element要用.text才能存取裡面的文字。如果要存什麼網址之類的，則是用get_attribute這種。
# 爬回內容：
# -------------------------------------
# 球 隊｜臺北達欣工程
# 背 號｜#21
# 位 置｜C
# 生 日｜1988-11-28
# 年 齡｜30 歲
# 身 高｜211 公分
# 體 重｜112 公斤
# -------------------------------------




tbl = driver.find_element_by_class_name("table-responsive")
a = tbl.find_elements_by_tag_name('td')
for i in a:
	print(i.text)
# 爬回：數據的部分
# -------------------------------------
# 30
# 7.5-12.3
# 60.59%
# 0-0.1
# 0%
# 2.8-4.8
# 59.3%
# 7.5-12.4
# 60.31%
# 17.8
# 13.6
# 0.6
# 1.7
# 0.3
# 2.6
# 1.9

# 36
# 1077
# 269-444
# 60.59%
# 0-2
# 0%
# 102-172
# 59.3%
# 269-446
# 60.31%
# 640
# 491
# 23
# 61
# 11
# 93
# 68
# -------------------------------------


driver.quit()
