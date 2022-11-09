import random
import time


def CompareAdd(List, Set):
    time1 = time.perf_counter()
    for i in range(10000):
        List.append(random.randint(0, 100000))
    time2 = time.perf_counter()
    for i in range(10000):
        Set.add(random.randint(0, 100000))
    time3 = time.perf_counter()
    return time2 - time1, time3 - time2


def CompareInsert(List, Set):
    time1 = time.perf_counter()
    for i in range(10000):
        List.insert(random.randint(0, len(List) - 1), random.randint(0, 100000))
    time2 = time.perf_counter()
    for i in range(10000):
        Set.add(random.randint(0, 100000))
    time3 = time.perf_counter()
    return time2 - time1, time3 - time2


def CompareContain(List, Set):
    cnt = 0
    time1 = time.perf_counter()
    for i in range(10000):
        number = random.randint(0, 100000)
        if number in List:
            cnt += 1
    time2 = time.perf_counter()
    cnt = 0
    for i in range(10000):
        number = random.randint(0, 100000)
        if number in Set:
            cnt += 1
    time3 = time.perf_counter()
    return time2 - time1, time3 - time2


def CompareRemove(List, Set):
    time1 = time.perf_counter()
    for i in range(10000):
        List.pop()
    time2 = time.perf_counter()
    for i in range(10000):
        Set.pop()
    time3 = time.perf_counter()
    return time2 - time1, time3 - time2


list = []
set = set()
listadd, setadd = CompareAdd(list, set)
listinsert, setinsert = CompareInsert(list, set)
listcontain, setcontain = CompareContain(list, set)
listremove, setremove = CompareRemove(list, set)
print("List添加所用时间:%.7lf\n"
      "Set添加所用时间: %.7lf\n" % (listadd, setadd))
print("List插入所用时间:%.7lf\n"
      "Set插入所用时间: %.7lf\n" % (listinsert, setinsert))
print("List判断所用时间:%.7lf\n"
      "Set判断所用时间: %.7lf\n" % (listcontain, setcontain))
print("List删除所用时间:%.7lf\n"
      "Set删除所用时间: %.7lf\n" % (listremove, setremove))
