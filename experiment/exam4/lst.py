class lst:
    list=[]
    def __init__(self,list):
        self.list=list
    def __add__(self, other):
        outcome=lst([])
        for i in range(min(len(self.list),len(other.list))):
            outcome.list.append(self.list[i]+other.list[i])
        if len(self.list)==len(other.list):
            return outcome
        elif len(self.list)>len(other.list):
            for i in range(len(other.list),len(self.list)):
                outcome.list.append(self.list[i])
            return outcome
        else:
            for i in range(len(self.list),len(other.list)):
                outcome.list.append(other.list[i])
            return outcome

if __name__ == '__main__':
    num=int(input("请输入要叠加的列表个数"))
    lstlist=[]
    for i in range(num):
        a=list(map(int,input("请输入第%d组数"%(i+1)).split()))
        lstlist.append(lst(a))
    outcome=lst([])
    for i in range(num):
        outcome=outcome+lstlist[i]
    print(outcome.list)