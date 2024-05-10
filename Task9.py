def card(number):
    for i in range(len(number)-4):
        print("*",end="")
    for j in range(len(number)-4,len(number)):
        print(number[j],end="")
number = input()
card(number)