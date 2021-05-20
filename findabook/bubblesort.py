def BubbleSort(list):
    p = len(list)
    if p>1:
        for i in range(p-1):
            for j in range(0, p-i-1):
                if list[j] > list[j+1] :
                    list[j], list[j+1] = list[j+1], list[j]
    else:
        list = list


int_list = [64] # This is a sample list used to test to test the code under "else" in the program

BubbleSort(int_list) # int_list is passed as a parameter through the procedure BubbleSort

print ("Sorted list is:") # The phrase "Sorted list is" is displayed
for i in range(len(int_list)):
    print ("%d" %int_list[i]) # prints the list of sorted numbers