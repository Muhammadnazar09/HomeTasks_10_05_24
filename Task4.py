import random
import random
one_list = []
two_list = []
suma=0
suma2=0
for i in range(6):
    f=random.randrange(10,30)
    m=random.randrange(10,30)
    suma+=f
    suma2+=m
    one_list.append(f)
    two_list.append(m)
print(one_list)
print(two_list)
if suma==suma2:
    print(True)
else:
    print(False)




# f = []
# m = []
# suma=0
# suma2=0
# for i in range(6):
#     f.append(random.randrange(10,30))
#     m.append(random.randrange(10,30))
# print(f)
# print(m)
# suma=0
# suma2=0
# for i in range(len(f)):
#     suma+=int(f[i])
#     suma2+=int(m[i])
# for i in range(len(m)):
#     suma2+=int(m[i])
# if suma==suma2:
#     print(True)
# else:
#     print(False)