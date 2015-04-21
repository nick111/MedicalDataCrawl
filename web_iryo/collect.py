# coding: utf-8

# python collect.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()

search_words_file_path = "search_words/search_words.txt"
html_dir = 'in_html/'

search_words = []

fr_words = open(search_words_file_path,'r')

for search_word in fr_words:
	search_words.append(search_word.strip())

for search_word in search_words:
	driver.get("http://rctportal.niph.go.jp/search")
	elem = driver.find_element_by_id("R01w02v01Keyword")
	elem.send_keys(Keys.BACK_SPACE * 100)
	elem.send_keys(search_word.decode('utf-8'))
	elem.send_keys(Keys.RETURN)
	no_result = False
	while(True):
		try:
			elem = driver.find_element_by_id('R01w03v01DisplayCount')
			break
		except:
			print("もういっかい")
			page = driver.page_source.encode('utf-8')
			if "データが見つかりませんでした。" in page:
				no_result = True
				break
	if no_result == True:
		continue
	select_obj = Select(elem)
	select_obj.select_by_visible_text(u'50件')
	page_i = 1
	page = driver.page_source
	fw = open(html_dir + search_word + str(page_i), 'a')
	fw.write(search_word + '\n')
	fw.write(page.encode('utf-8'))
	fw.close
	page_num = int(page.encode('utf-8').split('\n')[65].split("全")[1].split("ページ")[0])
	while page_i < page_num:
		page_i = page_i + 1
		driver.get("http://rctportal.niph.go.jp/result/page:" + str(page_i) + "/limit:50")
		page = driver.page_source
		fw = open(html_dir + search_word + str(page_i), 'a')
		fw.write(search_word + '\n')
		fw.write(page.encode('utf-8'))
		fw.close

driver.close()
