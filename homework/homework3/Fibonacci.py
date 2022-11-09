#当月总数=上个月数量（已有）+上上个月数量（新生）
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


print(f(12))
