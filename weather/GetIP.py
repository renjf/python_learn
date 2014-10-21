#!/usr/bin/env python  
# coding=utf-8  
# Python 2.7.3  
# File: GetIP.py  
# 获得外网IP地址  
import urllib2  
import httplib  

def GetIP():  
	response = urllib2.urlopen('http://ip.dnsexit.com/index.php')  
	htmlStr = response.read()  
	return htmlStr  
'''
# 测试代码 
print GetIP() 
'''
