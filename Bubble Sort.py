data=[10,9,8,7,6,5,4,3,2,1]
def bul(a):
    lengh=len(a)
    for i in range(len(a)-1):
        for j in range(lengh-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print(a)
    return a
bul(data)
d=[1,2,3,4,5,6,7,8,9,10]
def antibul(d):
    lengh=len(d)
    for i in range(len(d)-1):
        for j in range(lengh-1-i):
            if d[j]+1>d[j]:
              d[j+1],d[j]=d[j],d[j+1]
    print(d)
    return d
antibul(d)