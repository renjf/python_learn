#!/usr/bin/env python  
# coding=utf-8  
# Python 2.7.3  
import GetIP  
import GetCity  
import GetCityID  
import GetCityWeather  


def get_id_by_name(name):
	city_dic={};
	f=open("./config/city_id.txt")
	while True:
		line=f.readline();
		if line=='':
			break;
		if line[0]=='#' or line[0]=='\n':
			continue
    		city_list=line.replace("\n","").replace("\r","").split('\t')
		city_dic[city_list[0]]=city_list[1]
	f.close()	
	if name in city_dic:
		return city_dic[name];
	else:
		return ''

def print_weather_info(st):
	try:
		ss=st["weatherinfo"] 
		print u'城市：%s 日期：%s %s' %(ss["city"],ss["date_y"],ss["week"])

		print u'\t 今天\t\t 明天\t\t后天 '
		print u'温度：%s\t\t%s\t\t%s'%(ss["temp1"],ss["temp2"],ss["temp3"])
		print u'天气：%s\t\t%s \t\t%s'%(ss["weather1"],ss["weather2"],ss["weather3"])
		print u'风力：%s\t\t%s \t\t%s'%(ss["wind1"],ss["wind2"],ss["wind3"])
		
	except :
		print 'can not get weather information'
		

#联网后自动根据本机IP地址，查询归属地天气
def auto_get_weather_info():
	ip = GetIP.GetIP()  
	print ip  

	# 国家/省份/城市  
	city = ["", "", ""]  
	GetCity.GetCity(ip, city)  
	print city[0], city[1], city[2]  

	provinceURL=GetCityID.GetProvinceURL(city[1])  
	cityURL=GetCityID.GetCityURL(provinceURL, city[2])  
	print provinceURL  
	print cityURL  

#	st = GetCityWeather.GetCityWeather(cityURL)  
	st=GetCityWeather.SwitchGetCityWeather(cityURL)
	return st

#根据省份城市查询天气
def  weatherinfo_byname(city_name):
	city_id=get_id_by_name(city_name)
	if city_id=='':
		return ''
	cityURL="http://m.weather.com.cn/atad/%s.html"%(city_id);
	#st = GetCityWeather.GetCityWeather(cityURL)  
	st=GetCityWeather.SwitchGetCityWeather(cityURL)
	return st

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
#st=auto_get_weather_info()
st=weatherinfo_byname('常州')
#st=GetCityWeather.SwitchGetCityWeather("http://m.weather.com.cn/atad/101020100.html")
print_weather_info(st)

