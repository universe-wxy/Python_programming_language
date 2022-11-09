# gcd求解最大公倍数
def gcd(a, b):
    return a if b == 0 else int(gcd(b, a % b))


# lfm求解最小公倍数
# a,b 的最小公倍数 a * b / gcd(a, b)
def lfm(list, n):
    if n == 1:
        return list[1] * list[0] / gcd(list[1], list[0])
    a = lfm(list, n - 1)
    b = list[n - 1]
    return a * b / gcd(a, b)


while True:
    list = []
    a = int(input())
    b = int(input())
    c = int(input())
    list.append(a)
    list.append(b)
    list.append(c)
    # 将list进行排序，gcd中需要a>b
    list.sort(reverse=True)
    outcome = lfm(list, len(list))
    print(outcome)
