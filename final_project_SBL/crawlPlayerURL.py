from selenium import webdriver
import time

# 要爬的網頁
page = "https://sbl.choxue.com/stats"

# driver抓下來以後放的路徑
driver = webdriver.Chrome('/Users/evanyo25/Applications/Chrome Apps.localized/chromedriver')
driver.get(page)

# 給他開啟的時間，不留點時間網頁會還沒載好，會抓不到東西
time.sleep(5)



from selenium.webdriver.support.select import Select
Select(driver.find_element_by_id("sortable-menu")).select_by_visible_text("S14 例行賽")
time.sleep(5)


# 用 class name 去 find elements <--s 加s表示找多個
# 回傳一個 list of element 用 for 去展開他
tbl = driver.find_element_by_class_name("table-condensed")
a = tbl.find_elements_by_tag_name('a')
for i in a:
	print(i.text)
	print(i.get_attribute('href'))
# 爬回內容：
# ---------------------------------
# 梅奧
# https://sbl.choxue.com/player/9T8KdEG7HlK-svVTdoF1nQ
# 麥克連
# https://sbl.choxue.com/player/_GGDTifCtrkotU3Ui0dZNg
# ...
# ---------------------------------



driver.quit()


# 用來滑動滾輪
# print('start_scrolling')
# for i in range(100):
# 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 	time.sleep(0.5)
# print('end_scrolling')