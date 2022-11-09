import urllib.request
content=urllib.request.urlopen("http://www.edu.cn")
print("http header: " ,content.info())
print("http status: " ,content.getcode())
print("url: " ,content.geturl())
i=0
print("content:")
for line in content.readlines():
    print(line.decode('utf-8'))
    i=i+1
    if i >20:
        break
