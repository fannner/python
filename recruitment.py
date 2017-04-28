mport requests,json,re,string
#　获取招聘的页数
def getPage(city, keyword):
	url = "http://www.lagou.com/jobs/list_%s?city=%s" %(keyword, city) 
	pageData = requests.get(url).text 
	pageNum = int(re.findall(r'<span class="span totalNum">(.*)</span>',pageData)[0]) 
	return pageNum

# 获取一页的招聘信息
def getOne(city, keyword, pageNum):
	url = "http://www.lagou.com/jobs/positionAjax.json?city=%s&needAddtionalResult=false&pn=%d&kd=%s" %(city, pageNum, keyword) 
	data = json.loads(requests.get(url).text) 
	return data['content']['positionResult']['result']

# 获取多页的招聘信息
def getList(city, keyword, pageNum): 
	pageNum = {0:pageNum,1:getPage(city, keyword)} 
	pageNum = pageNum[0] if pageNum[1] > pageNum[0] else pageNum[1] 
	infoList = [] 
	for pn in range(1,pageNum+1): 
		infoList.extend(getOne(city, keyword, pn))
		#print('[%d] OK' %pn) 
		for singleList in infoList:
			#print('%s' %type(singleList))
			for oneParam in singleList:
				if oneParam == 'companySize':
					print('================招聘信息分割线=====================')
				print('%s:%s' %(oneParam,singleList[oneParam]))
	#print('总爬取页数:%d 总爬取职位数:%d' %(pageNum, len(infoList)))

getList('北京','java',500)
