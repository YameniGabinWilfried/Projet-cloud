def removefromlist(myList, nbr):  # remove all the occurences of an element in the list
    i = 0
    j = 0
    n = len(myList)
    key = myList[i]
    while i < n:
        if myList[i] == nbr:
            myList.remove(nbr)
            n = len(myList)
            i = 0
        else:
            i += 1
    return myList


def isdouble(myList):  # verify if there is no double value in a list
    i = 0
    j = 1
    n = len(myList)
    while i < n - 1:
        j = i + 1
        while j < n:
            if myList[i] == myList[j]:
                return True
            j += 1
        i += 1
    return False


# fill the list until the user enters stop.
myList = []
values = ''
while values != 'stop':
    values = input("> ") # Enter a value that will figure in the list
    myList.append(values)
print("The reptitive values are:", end='  ')

# we firstly verify if there is any double value in the list. If so we enter into
# the while loop. Then if we find that a value is equal to any other value, we call
# the removefromlist function to clear that value in the list and to print that value
# if it's true, i become again 0, and j is stable (1).
i = 0
n = len(myList)
if not isdouble(myList):
    print('none')
else:
    while isdouble(myList):
        # if (myList[i] == myList[j] and i < n - 1):
        #     value = myList[i]
        #     print(value, end=' ')
        #     removefromlist(myList, myList[i])
        #     i = 0
        # elif i > n - 1 and len(myList) != 0:
        #     i = 0
        #     j += 1
        # elif len(myList) == 0:
        #     break
        # else:
        #     i += 1
        val=myList[i]
        nbr=myList.count(val)
        if nbr!=1:
            print(myList[i], end=' ')
            removefromlist(myList, val)
        elif i < n and len(myList) != 0:
            i+=1
        else:
            break
