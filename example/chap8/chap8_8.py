
import sys
import urllib.request
import re

url='http://www.edu.cn'
res=urllib.request.urlopen(url)
htm=res.read()
details=htm.decode('utf-8')

linkPattern=re.compile("a href=\"(.+?)\"")
links=linkPattern.findall(details)
print("网页链接总数=",len(links))

imagePattern=re.compile("img src=\"(.+?)\"")
images=imagePattern.findall(details)
print("图片总数=",len(images))