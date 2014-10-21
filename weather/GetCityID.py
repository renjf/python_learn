#!/usr/bin/env python  
# coding=utf-8  
# Python 2.7.3  
# File: GetCityID.py  
# 获取城市的天气的URL地址  
import urllib2  
import HTMLParser  
import httplib  
from bs4 import BeautifulSoup  

def GetProvinceURL(province):  
	response = urllib2.urlopen('http://www.weather.com.cn/textFC/hn.shtml')  
	htmlByte = response.read()  
	htmlStr = htmlByte.decode("utf8")  
	soup2 = BeautifulSoup(htmlStr)  
	div = soup2.find("div", class_ = "lqcontentBoxheader")  
	lista = div.find_all("a")  
	provinceURL = "http://www.weather.com.cn"  
	for aItem in lista:  
		if aItem.text == province:  
			provinceURL = provinceURL + aItem["href"]  
			break  

	return provinceURL  

def GetCityURL(provinceURL, city):  
	response = urllib2.urlopen(provinceURL)  
	htmlByte = response.read()  
	htmlStr = htmlByte.decode("utf8")  

	soup2 = BeautifulSoup(htmlStr)  
	div = soup2.find("div", class_ = "hanml")  
	lista = div.find_all("a", text = city)  
	cityURL = lista[0]["href"].replace("www.weather.com.cn/weather", "m.weather.com.cn/data")  
	cityURL = cityURL.replace("shtml", "html")  
	return cityURL  
	''''' 
# GetProvinceURL 测试代码 
	print GetProvinceURL(u"广东") 
	'''  
# GetProvinceURL 测试代码  
provinceURL = GetProvinceURL(u"广东")  
print provinceURL  
cityURL = GetCityURL(provinceURL, u"广州")  
print cityURL  
