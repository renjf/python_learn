#!/usr/bin/env python  
# coding=utf-8  
# Python 2.7.3  
# File: GetCityWeather.py  
# 获得城市天气数据  
import urllib2  
import httplib  
import json  
import os
import time

ONEHOURSEC=60*60

def judge_cachefile_chekout_time(filename):
	last_modify_time=os.path.getmtime(filename)
	now_time=time.time()
	last_date=time.strftime('%Y-%m-%d',time.localtime(last_modify_time)) 
	now_date=time.strftime('%Y-%m-%d',time.localtime(now_time))
	
	if last_date != now_date:
		#第二天更新缓存
		return True
	elif abs(now_time - last_modify_time)>=6*ONEHOURSEC:
		#文件超过 6小时 更新缓存
		return True
	else:
		return False
	
def SwitchGetCityWeather(cityURL):
	if cityURL=='':
		return ''
	name_map=cityURL.split('/');
	file_name='./data/%s'%(name_map[-1]);
	if os.path.exists(file_name):
		#判断缓存文件是否超时
		if judge_cachefile_chekout_time(file_name)==True:
			st=GetCityWeather(cityURL)	
			return st
		else:
			#未超时，直接读取缓存文件
			st=GetCityWeather_byfile(file_name)
			return st
	else:
		st=GetCityWeather(cityURL)	
		return st

def GetCityWeather_byfile(html_file):
	if html_file=='':
		return ''
	print 'GetCityWeather: %s ' %(html_file)
	try:
		fp_r=open(html_file,"r");
		htmlByte=fp_r.readline();
		htmlStr = htmlByte.decode("utf8") 
		st = json.loads(htmlStr);  
		fp_r.close()
		return st 
	except:
		return ''

def GetCityWeather(cityURL): 
	if cityURL=='':
		return ''
	try:
		print 'GetCityWeather: %s ' %(cityURL)
		try:
			i_headers ={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',"Referer":'http://www.weather.com.cn'} 
			req=urllib2.Request(cityURL,headers=i_headers)
			response = urllib2.urlopen(req) 
			htmlByte = response.read() 
			htmlStr = htmlByte.decode("utf8") 
			st = json.loads(htmlStr);  
			save_weather_html(htmlByte,cityURL) 
			return st 
		except urllib2.HTTPError, e:
			print e.code
			return ''
	except:
		st='';  
		return st
	''''' 
# http://m.weather.com.cn/data/101280101.html 
{"weatherinfo":{"city":"广州","city_en":"guangzhou","date_y":"2013年11月29日","date":"","week":"星期五","fchh":"11","cityid":"101280101","temp1":"18℃~5℃","temp2":"20℃~7℃","temp3":"21℃~8℃","temp4":"21℃~9℃","temp5":"22℃~10℃","temp6":"23℃~10℃","tempF1":"64.4℉~41℉","tempF2":"68℉~44.6℉","tempF3":"69.8℉~46.4℉","tempF4":"69.8℉~48.2℉","tempF5":"71.6℉~50℉","tempF6":"73.4℉~50℉","weather1":"晴","weather2":"晴","weather3":"晴","weather4":"晴","weather5":"晴","weather6":"晴","img1":"0","img2":"99","img3":"0","img4":"99","img5":"0","img6":"99","img7":"0","img8":"99","img9":"0","img10":"99","img11":"0","img12":"99","img_single":"0","img_title1":"晴","img_title2":"晴","img_title3":"晴","img_title4":"晴","img_title5":"晴","img_title6":"晴","img_title7":"晴","img_title8":"晴","img_title9":"晴","img_title10":"晴","img_title11":"晴","img_title12":"晴","img_title_single":"晴","wind1":"北风3-4级转微风","wind2":"微风","wind3":"微风","wind4":"微风","wind5":"微风","wind6":"微风","fx1":"北风","fx2":"微风","fl1":"3-4级转小于3级","fl2":"小于3级","fl3":"小于3级","fl4":"小于3级","fl5":"小于3级","fl6":"小于3级","index":"较冷","index_d":"建议着大衣、呢外套加毛衣、卫衣等服装。体弱者宜着厚外套、厚毛衣。因昼夜温差较大，注意增减衣服。","index48":"较冷","index48_d":"建议着大衣、呢外套加毛衣、卫衣等服装。体弱者宜着厚外套、厚毛衣。因昼夜温差较大，注意增减衣服。","index_uv":"中等","index48_uv":"中等","index_xc":"适宜","index_tr":"适宜","index_co":"舒适","st1":"16","st2":"6","st3":"19","st4":"8","st5":"20","st6":"9","index_cl":"不宜","index_ls":"适宜","index_ag":"易发"}} 
'''  

def save_weather_html(content,cityURL):
	
	name_map=cityURL.split('/');
	file_name='./data/%s.tmp'%(name_map[-1]);
	dst_file_name='./data/%s'%(name_map[-1]);
	try:
		fp_w=open(file_name,"w")
		fp_w.write(content);
		fp_w.close()	
		os.rename(file_name,dst_file_name)		
		print
	except :
		print 'save file error'

# GetCityWeather测试代码 
# GetProvinceURL 测试代码
#cityURL = "http://m.weather.com.cn/atad/101280101.html" 
''''
cityURL = "http://m.weather.com.cn/atad/101020100.html"
st=SwitchGetCityWeather(cityURL);
print cityURL
ss = st["weatherinfo"] 
print ss["city"] 
print ss["date_y"] 
print ss["week"] 
print ss["temp1"] 
print ss["weather1"] 
'''

''''' 
# 输出 
	广州 
	2013年11月29日 
	星期五 
	18℃~5℃ 
	晴 
	'''  
