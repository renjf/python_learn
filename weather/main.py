#!/usr/bin/env python  
# coding=utf-8  
# Python 2.7.3  
import GetIP  
import GetCity  
import GetCityID  
import GetCityWeather  


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
ss = st["weatherinfo"]  
print ss["city"]  
print ss["date_y"]  
print ss["week"]  
print ss["temp1"]  
print ss["weather1"]  
