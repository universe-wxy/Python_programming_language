import datetime
class Date:
    def __init__(self,year,month,date):
        self.__year=year
        self.month=month
        self.date=date

    def getyear(self):
        return self.__year
    def getmonth(self):
        return self.month
    def getdate(self):
        return self.date
    def setyear(self,year):
        self.__year=year

    def __repr__(self):
        return "%d.%d.%d"%(self.__year,self.month,self.date)

if __name__ == '__main__':
    dateobject=datetime.datetime.now()
    date=Date(int(dateobject.year),int(dateobject.month),int(dateobject.day))
    print(date)
    date.setyear(2033)
    print(date)