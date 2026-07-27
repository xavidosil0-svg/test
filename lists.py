list_name=[1,7,8,4,92,5]
print(list_name)
list_name[3]=19
print(list_name[3])
list_name.append(32**2)
# Get and store input. ADD input to the list.
x=input("what do you want to add to your list?")
list_name.append(x)
print(list_name)
while(True):
    x=input("what do you want to add to your list?")
    list_name.append(x)
    y=input("do you want to continue?")
    if y=="no":
        break