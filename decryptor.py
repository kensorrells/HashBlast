import hashlib

a = 0
b = 0
cant = ''
i = 0
x = 0
chrlist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           ' ','1','2','3','4','5','6','7','8','9','0']

cent = input(str('Input code: '))
while x <= len(cent):
    while i+x <= x+39:
        cant += cent[i+x]
        i += 1
    i = 0
    while a <= 62:
        b = chrlist[a]
        b =  hashlib.sha1(b.encode()).hexdigest()
        if cant == b:
            print(chrlist[a])
            a = 100
        else:
            a += 1
    a = 0
    cant = ''
    x += 40
