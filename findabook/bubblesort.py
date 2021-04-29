def BubbleSort(int_list):
    p = len(int_list)
    for i in range(p-1):
        for j in range(0, p-i-1):
            if int_list[j] > int_list[j+1] :
                int_list[j], int_list[j+1] = int_list[j+1], int_list[j]

int_list = [64, 34, 25, 12, 22, 11, 90]

BubbleSort(int_list)

print ("Sorted array is:")
for i in range(len(int_list)):
    print ("%d" %int_list[i])