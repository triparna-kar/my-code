# Visualization: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html

mylist = [40, 98, 67, 2, 89, 13, 10, 0, 82, 39, 4]
# mylist = [3, 2, 1]

def insertionsort(mylist):
    for i in range(len(mylist)-1):
        for j in range(i,-1,-1):
            num = mylist[j]
            next = mylist[j+1]
            if next < num:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
            else:
                break
            
        print("After Iteration: {}:\n".format(i) + str(mylist))        
insertionsort(mylist)
print("Final list: "+ str(mylist))