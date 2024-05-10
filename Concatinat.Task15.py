def concatinat(a,b):
    str1=''
    suma=0
    if a==int(a) and b==int(b):
        str1+=str(a)+str(b)
        return str1
    elif a==str(a) and b==str(b):
        suma+=int(a) + int(b)
        return suma
    elif a==int(a) and b==str(b) or b==int(b) and a==str(a):
        return False
print(concatinat("5","10"))