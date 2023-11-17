a=float((input('你的體重')))
b=float(input('你的身高'))
print("your BMI=")
print(a/(b/100)**2)
if(a/(b/100)**2<18.5):{print("體重過輕")}
if(a/(b/100)**2>24):{print("體重過重")}
if(18.5<a/(b/100)**2<24):{print("體重正常")}


