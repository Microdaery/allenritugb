import math
a=input('enter a number')
try:
    a=float(a)
    if(a>10):
        print('you number is large than 10','you number sqrt is',math.sqrt(a))
    elif(a>0):
        print('you number is positive and you number sqare is',a**2)
    elif(a==0):
        print('you number is zero,0')
    else:
        print('you number is negative and you number sqare is',a**2)        
except:
    print('enter a number')

