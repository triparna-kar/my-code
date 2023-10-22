def insertionsort(mylist):
    length = len(mylist)
    for i in range(1, length):
        j = i-1
        key = mylist[i]
        while(j>=0 and mylist[j]>key):
            mylist[j+1] = mylist[j]
            j = j - 1
            mylist[j+1] = key
            