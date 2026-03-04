def modify_tuple(tupl, newElem):

    list =[]

    for element in tupl:
        list.append(element)    #list(tupl) also works but I wanted to show how to do it with a loop.

    list.append(newElem)   

    return tuple(list)


tupl = (1, 2, 3, 4, 5)
print(tupl)

print("What do you want to add to the tuple?")
elem= int(input("Eklenecek element:" ))
#first we have to turn the tuple to a list, then we can add the new element to the list and finally we can turn it back to a tuple and return it.
newTupl = modify_tuple(tupl, elem)
print("The new tuple is ", newTupl)


