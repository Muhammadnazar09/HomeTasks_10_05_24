import random
n = int(input())
my_list = []
for i in range(n):
    my_list.append(random.randrange(100,300))
print(my_list)
big = my_list[0]
for i in my_list:
    if i>big:
        big=i
print(big)