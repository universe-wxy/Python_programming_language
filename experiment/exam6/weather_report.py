import matplotlib.pyplot as plt
import requests
import json


class TypeException(Exception):
	pass


# 函数式编程
class weather_report:
	# 数据获取与整理
	# 完成初始化
	def __init__(self, city) -> None:
		# 连接接口 获取数据
		self.url = url = "http://t.weather.itboy.net/api/weather/city/{}".format(city)
		self.req = requests.get(url)
		self.result = json.loads(self.req.text)

	#显示实时信息
	def realtime_info(self) -> None:
		# 整理数据
		print("下面展示当前城市的实时天气信息：\n")
		print("城市:       ".ljust(20),
			  "{}省{}\n".format(self.result['cityInfo']['parent'], self.result['cityInfo']['city']) +
			  "当前气温:    ".ljust(20), "{}\n".format(self.result['data']['wendu']) +
			  "空气湿度:    ".ljust(20), "{}\n".format(self.result['data']['shidu']) +
			  "pm2.5含量:  ".ljust(20), "{}\n".format(self.result['data']['pm25']) +
			  "空气质量:    ".ljust(20), "{}\n".format(self.result['data']['quality']))

	def Week_Info(self) -> None:
		print("下面展示一周内的天气信息（包括昨天）")
		temp = self.result['data']['yesterday']
		print("日期:{:10s}    ".format(temp['ymd']),
			  "当日最{:7s}   ".format(temp['high']),
			  "当日最{:7s}    ".format(temp['low']),
			  "当日日出时间:{:7s}    ".format(temp['sunrise']),
			  "当日日落时间:{:7s}    ".format(temp['sunset']),
			  "风向为:{:5s}  风力为:{:5s}     ".format(temp['fx'], temp['fl']),
			  "当日天气类型为:{:5s}".format(temp['type']))
		for i in range(6):
			temp = self.result['data']['forecast'][i]
			print("日期:{:10s}    ".format(temp['ymd']),
				  "当日最{:7s}   ".format(temp['high']),
				  "当日最{:7s}    ".format(temp['low']),
				  "当日日出时间:{:7s}    ".format(temp['sunrise']),
				  "当日日落时间:{:7s}    ".format(temp['sunset']),
				  "风向为:{:5s}  风力为:{:5s}     ".format(temp['fx'], temp['fl']),
				  "当日天气类型为:{:5s}".format(temp['type']))

	def More_Info(self) -> None:
		print("下面展示15天内的天气信息")#设置15天为时间范围
		temp = self.result['data']['forecast']
		for i in range(len(temp)):
			print("日期:{:10s}    ".format(temp[i]['ymd']),
				  "当日最 {:7s}   ".format(temp[i]['high']),
				  "当日最 {:7s}    ".format(temp[i]['low']),
				  "当日日出时间:{:7s}    ".format(temp[i]['sunrise']),
				  "当日日落时间:{:7s}    ".format(temp[i]['sunset']),
				  "风向为:{:5s}  风力为:{:5s}     ".format(temp[i]['fx'], temp[i]['fl']),
				  "当日天气类型为:{:5s}".format(temp[i]['type']))

	def Weather_Change(self) -> None:
		print("下面展示气温变化曲线图")
		x = []
		y_h = []
		y_l = []
		temp = self.result['data']['forecast']
		for i in range(len(temp)):
			x.append(temp[i]['ymd'])
			y_h.append(int(temp[i]['high'][3:5].strip('℃')))#向列表添加数据并去除原数据中的“℃”
			y_l.append(int(temp[i]['low'][3:5].strip('℃')))
		plt.plot(x, y_h, label='最高气温', color='r')#设置x，y数值，内容标签为最高气温，曲线为红色
		plt.plot(x, y_l, label='最低气温', color='b')#设置x，y数值，内容标签为最低气温，曲线为蓝色
		plt.xticks(rotation=90)#旋转90°
		plt.xlabel('日期')#横轴为日期
		plt.ylabel('气温')#纵轴为气温
		plt.title('气温变化曲线图')#设置统计图标题
		plt.legend()#根据可见对象和标签自动构造图例
		plt.show()#显示统计图

	def aqi_Change(self) -> None:
		print("下面展示空气质量变化")
		x = []
		y = []
		temp = self.result['data']['forecast']
		for i in range(len(temp)):
			x.append(temp[i]['ymd'])
			y.append(int(temp[i]['aqi']))
		plt.plot(x, y, label="空气质量变化曲线", color='g')
		plt.xlabel('日期')
		plt.ylabel('空气质量指数')
		plt.xticks(rotation=90)
		plt.title('空气质量变化曲线')
		plt.legend()
		plt.show()


if __name__ == '__main__':
	# 显示面板信息
	print("请选择您所在的城市代码:")
	print("101010100-北京\n"
		  "101020100-上海\n"
		  "101280101-广州\n"
		  "101220101-合肥\n"
		  "101210101-杭州\n"
		  "101121301-威海\n")
	# 获取用户输入
	city = int(input())
	ans = weather_report(city)
	ans.realtime_info()
	#数据分析展示
	while True:
		# 获取用户输入
		print("请输入您要显示的信息")
		print("1-一周内(从昨天起)天气信息\n"
			  "2-15天内(含当天)天气信息\n"
			  "3-气温变化曲线图\n"
			  "4-空气质量变化\n")
		choice = int(input())
		try:
			if choice == 1:
				ans.Week_Info()
			elif choice == 2:
				ans.More_Info()
			elif choice == 3:
				ans.Weather_Change()
			elif choice == 4:
				ans.aqi_Change()
			else:
				raise TypeException
		except TypeException:#按异常类名捕获异常
			print("输入的选择有误，请重试")
		print()
		print()
