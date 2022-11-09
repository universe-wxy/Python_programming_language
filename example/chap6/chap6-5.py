import pickle
data={'Jack':[32,'male','market'],'Suan':[28,'female','AD.']}
L=[1,2,3]
L.insert(1,'zxd')
with open('d:\\pythontest\\p1.txt','wb') as f:
    pickle.dump(data,f)
    pickle.dump(L,f,-1)
with open('d:\\pythontest\\p1.txt','rb') as f:
    data=pickle.load(f)
    print(data)
    L=pickle.load(f)
    print(L)
