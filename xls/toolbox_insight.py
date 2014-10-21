#FileName: toolbox_insight.py
from sgmllib import SGMLParser
import threading
import time
import urllib2
import StringIO
import gzip
import string
import os
#rewrite SGMLParser for start_a
class Basegeturls(SGMLParser):   #这个Basegeturls类作用是分析下载的网页，把网页中的所有链接放在self.url中。
				  def reset(self):
	self.url = []
	SGMLParser.reset(self)
	def start_a(self, attrs):
		href = [v for k, v in attrs if k == 'href']
	if href:
	self.url.extend(href)
#for quickly finding
	class Newlist(list):#这个类其实是一个添加了find方法的LIST。当num变量在LIST中，返回True,当不在LIST中，返回False并把num按二分法插入LIST中
		       def find(self, num):
			       l = len(self)
	     first = 0
	   end = l - 1
	   mid = 0
	   if l == 0:
	   self.insert(0,num)
	   return False
	   while first < end:
	   mid = (first + end)/2
	   if num > self[mid]:
	   first = mid + 1
	   elif num < self[mid]:
	   end = mid - 1
	   else:
	  break
	 if first == end:
	   if self[first] > num:
	   self.insert(first, num)
	   return False
	   elif self[first] < num:
	   self.insert(first + 1, num)
	   return False
	   else:
		   return True
	elif first > end:
	self.insert(first, num)
	return False
	else:
		return True
