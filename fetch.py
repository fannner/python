#! /usr/bin/env python
#coding=utf-8
import sys 
import urllib2
import urllib
import requests
import cookielib

reload(sys)
sys.setdefaultencoding("utf8") 

## cookieHeader里面配置自己浏览器登录后产生的coookie,如果这个cookie过期时间很短，可能会有问题
cookieHeader = {"cookie":'JSESSIONID=F8AD82AD51D77C22C29E18771B058A3A; COOKIE_LASTROLEID=1; COOKIE_MANAGECODE_ADMIN=""; COOKIE_REMMANAGECODE_ADMIN=""; COOKIE_MANAGEPSW_ADMIN=""; COOKIE_AUTOMANAGELOGIN_ADMIN=""'}

##这里是具体需要抓取的url
inputUrl= 'http://112.109.196.142:8295/sfsp/query.do?menuitemId=604020&pageSize=100&id=214&refresh=0&parMap.BEG_DATE=2016-08-01&NULL=&parMap.END_DATE=2016-12-01&NULL=&parMap.MEMBER_ID=&parMap.WARE_ID=&parMap.BUY_SALE=&parMap.BUILD_FLAT=&parMap.OPER_TYPE=&method%3Alist=%E6%9F%A5%E8%AF%A2';

class Fetch(object):

	def __init__(self):
		self.cj = cookielib.LWPCookieJar()
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
		urllib2.install_opener(self.opener)
		self.url = inputUrl
		self.headers = cookieHeader
	
	def fetchData(self):
		req = urllib2.Request(self.url, headers=self.headers)
		response = urllib2.urlopen(req)
		self.operate = self.opener.open(req)
		data = response.read()
		print("%s" %data)

if __name__ == '__main__':
	handle = Fetch()
	handle.fetchData();
