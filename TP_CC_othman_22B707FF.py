





def getElement(Tab):
    k =0

    for pos,i  in enumerate(Tab):
        k += 1
        # print(k)
        if (Tab != []) :
            for j in Tab[pos+1::]:
                if j == i :
                    Tab=[m for m in Tab if m != i]
                    #(Tab)
                    return i,Tab
        else:
            return False

i = ""
mainTab =[]

while i != "exit":

    i = input("enter un val = ")
    if i != "exit":
        mainTab.append(i)
        print(mainTab)


#mainTab = [1,2,2,3,4,5,5,6,6,6,1,3]

while getElement(mainTab):
    x, mainTab = getElement(mainTab)
    print(x)