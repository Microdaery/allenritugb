n = int(input())
arr = map(int, input().split())
a=list(arr)
for j in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i]<a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print[a]
for c in range(len(a)-1):
    if (a[c]==a[c+1]):
        c=c+1
    elif (a[c]>a[c+1]):
        print(a[c+1])
        break
