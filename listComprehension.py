# Example 1
fruits = ['apple', 'banana', 'orange', 'strawberry']
newlist = []


for x in fruits:
    if "b" in x:
        newlist.append(x)

print(newlist)
#
# newlist = [expression for item in iterable if condition == True]
#
# expression / for item in iterable / if condition == True

newlist = [x.upper() for x in fruits if "b" in x]
print(newlist)

newlist2 = ['hello' for x in fruits]
print(newlist2)

newlist3 = [x if x != "banana" else "apple" for x in fruits]
print(newlist3)




