# Visualization: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html

mylist = [40, 98, 67, 2, 89, 13, 10, 0, 82, 39, 4]
# mylist = [3, 2, 1]

def selectionsort(mylist):
    for i in range(len(mylist)):
        lowest_index = i
        for j in range(i,len(mylist)):
            if mylist[j] < mylist[lowest_index]:
                lowest_index = j
        if lowest_index != i:
            mylist[i], mylist[lowest_index] = mylist[lowest_index], mylist[i]


selectionsort(mylist)
print("Final list: "+ str(mylist))