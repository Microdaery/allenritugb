##s=str(input('>'))
s='cpple'
ss="   Hello Allen   "
f=ss.strip()
mail='allen riyugb@gmail com'
if s=='cpple':
    print('found it ,apple')
elif s<'cpple':
    print('you word',s,', come before apple')
elif s>'cpple':
    print('you word',s,',comes after apple')
else:
    print('all right')
a=s.lower()
print(a)
b=s.find('a')
c=s.find('b')
d=s.find('p')
print(b,c,d)
e=s.replace('c','a')
print (e)
print(ss.lstrip())##去頭空白
print(ss.rstrip())##去尾空白
print(ss.strip())
print(ss.startswith(' '))
print(ss.startswith('H'))
print(f.startswith('Hello'))
ma=mail.find('@')
print(ma)
mb=mail.find(' ',ma)
print(mb)
prin=mail[ma+1:mb]
print(prin)