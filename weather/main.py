#!/usr/bin/env python  
# coding=utf-8  
# Python 2.7.3  
import GetIP  
import GetCity  
import GetCityID  
import GetCityWeather  

def print_weather_info(st):
	try:
		ss = st["weatherinfo"] 
		print '城市：%s 日期：%s %s 温度：%s 天气：%s' %(ss["city"],ss["date_y"],ss["week"],ss["temp1"],ss["weather1"]  )
	except:
		print 'can not get weather information'
		

def auto_get_weather_info():
	ip = GetIP.GetIP()  
	print ip  

	# 国家/省份/城市  
	city = ["", "", ""]  
	GetCity.GetCity(ip, city)  
	print city[0], city[1], city[2]  

	provinceURL = GetCityID.GetProvinceURL(city[1])  
	cityURL = GetCityID.GetCityURL(provinceURL, city[2])  
	print provinceURL  
	print cityURL  

	st = GetCityWeather.GetCityWeather(cityURL)  
	#st = GetCityWeather.SwitchGetCityWeather(cityURL) 
	print_weather_info(st) 

def  weatherinfo(city1,city2):
	provinceURL = GetCityID.GetProvinceURL(city1)  
	cityURL = GetCityID.GetCityURL(provinceURL, city2)  
	print provinceURL  
	print cityURL  

	st = GetCityWeather.GetCityWeather(cityURL)  
	print_weather_info(st) 

''''
fp_r=open('./config/province_city_id.txt',"r");
while True:
	line=fp_r.readline().decode("utf-8")
	if line == '':
		break;
	if line[0] =='\n' or line[0] =='#':
		continue
	city_map=line.replace('\n','').replace('\r','').split('\t')
	print '%s %s' %(city_map[0],city_map[1])
	weatherinfo(city_map[0],city_map[1])
'''
auto_get_weather_info()
