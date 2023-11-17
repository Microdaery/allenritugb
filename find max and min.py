a=-1
count=0
sum=0
f=False
b=int(input('>'))
print('before',a)
for i in [75,12,58,30,99,52,86,39,10,4,85]:
    count=count+1
    sum=sum+i
    if a<i:
        a=i
    if i==b:
        f=True
    print(count,i,sum,f)
print('after',a,'avg=',(sum/count))
c=None
print('before',c)
for i in [75,12,58,30,99,52,86,39,10,4,85]:
    count=count+1
    sum=sum+i
    if c==None:
        c=i 
    elif c>i:
        c=i
    if i==b:
        f=True
    print(count,i,sum,f)
print('after',c,'avg=',(sum/count))
