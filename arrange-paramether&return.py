name=input('your name ')
def thing(lang):
    if lang=='en':
        b='hello'
    elif lang=='fr':
        b='bonjour'
    elif lang=='cn':
        b='你好'
    else:
        b='hello'
    return b
def age(c,d):
    min=d-c
    return min
a=input('your lang(en,fr,cn) ')
print(thing(a),name)
if thing(a)=='hello':
    a1=int(input('how old are you '))
    a2=int(input('What year is this year? '))
    age(a1,a2)
    print('you born in ',age(a1,a2))
elif thing(a)=='你好':
    a1=int(input('你今年多大 '))
    a2=int(input('今年西元幾年 '))
    age(a1,a2)
    print('你出生在 ',age(a1,a2))
elif thing(a)=='bonjour':
    a1=int(input('Quel âge as-tu '))
    a2=int(input('En quelle année est cette année ? '))
    age(a1,a2)
    print('es-tu né en ',age(a1,a2))
else:
    a1=int(input('how old are you '))
    a2=int(input('What year is this year? '))
    age(a1,a2)
    print('you born in ',age(a1,a2))