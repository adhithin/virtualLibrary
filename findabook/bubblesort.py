def BubbleSort(list):
    p = len(list)
    if p>1:
        for i in range(p-1):
            for j in range(0, p-i-1):
                if list[j] > list[j+1] :
                    list[j], list[j+1] = list[j+1], list[j]
    else:
        list = list


int_list = [64]

BubbleSort(int_list)

print ("Sorted list is:")
for i in range(len(int_list)):
    print ("%d" %int_list[i])