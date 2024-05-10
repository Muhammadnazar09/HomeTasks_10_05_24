def ant(a,b,c):
    suma=0
    while a<=b:
        if a%c==0:
            suma+=a
            print(a,end=" ")
        a+=1
    print(end="\n")
    print(suma)
a,b,c=int(input()),int(input()),int(input())
ant(a,b,c)