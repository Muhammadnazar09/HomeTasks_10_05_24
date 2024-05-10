# my_dict = {"Darth Vader":"father",
#            "Leia":"sister",
#            "Han":"brozer in law",
#            "R2D2":"droid"}
# name = input()
# for k in my_dict.keys():
#     if k==name:
#         print(f"Luke, i am your {my_dict[k]}")

def dicta(name):
    my_dict = {"Darth Vader":"father",
           "Leia":"sister",
           "Han":"brozer in law",
           "R2D2":"droid"}
    print(f"fLuke, i am your {my_dict[name]}")
n = input()
dicta(n)