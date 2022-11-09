import math

def PrimeJudge(data):
    for i in range(2, int(math.sqrt(data)) + 1):
        if data % i == 0:
            return False
    return True

def RemovePrime(list):
    outcome = []
    for i in range(len(list)):
        if PrimeJudge(list[i]):
            continue
        else:
            outcome.append(list[i])
    return outcome

s = list(map(int, input("请输入数组").split(" ")))
outcome = RemovePrime(s)
print(outcome)
