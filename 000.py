lower = 100
upper = 200
for num in range(lower, upper+1):
    for i in range(2, num):
      if num % i == 0:
        break
    else:  #for 搭配else 會在跑完迴圈最後一圈之後執行else裡面的程式
        print(num)