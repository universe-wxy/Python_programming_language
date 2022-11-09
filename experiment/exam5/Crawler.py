import urllib3
class Crawler:
    ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'}
    def __init__(self,url):
        self.url=url
        self.http=urllib3.PoolManager()
        self.timeout=urllib3.Timeout(connect=1.0, read=3.0)
        self.req=self.http.request('GET',url,headers=self.ua,timeout=self.timeout,retries=5,redirect=4)

    def revhead(self):
        print(self.req.headers)
        return self.req.headers

    def revbody(self,file):
        with open(file,'w') as f:
            f.write(self.req.data.decode('gbk'))
            f.close()

    def __del__(self):
        print("退出")
        #print("爬取{}的爬虫类已析构".format(self.url))
        return True

def testWeb():
    crawler=Crawler('http://httpbin.org/get')
    crawler.revhead()
    crawler.revbody('./body.txt')
    del crawler

if __name__ == '__main__':
    testWeb()