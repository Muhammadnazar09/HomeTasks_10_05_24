my_str = input()
new_str=""
new_str1=""
new_str2=""
a="#"
b="?"
c="*"
for i in range(len(my_str)):
    if my_str[i]=="A" or my_str[i]=="a" or my_str[i]=="E" or my_str[i]=="e" or my_str[i]=="I" or my_str[i]=="i" or my_str[i]=="O" or my_str[i]=="o" or my_str[i]=="U" or my_str[i]=="u" or my_str[i]=="Y" or my_str[i]=="y":
        new_str+=a
        new_str1+=b
        new_str2+=c
    else:
        new_str+=my_str[i]
        new_str1+=my_str[i]
        new_str2+=my_str[i]
print(new_str)
print(new_str1)
print(new_str2)