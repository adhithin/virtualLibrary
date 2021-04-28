def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i] > nlist[i+1]:
                nlist[i],nlist[i+1] = nlist[i+1],nlist[i]

def testBubbleSort():
    nlist_num = [98, 17, 25, 63, 3, 77, 40, 16]
    nlist_char = ['u','e','a','i','o']
    nlist_str = ['ron','harry','hermione','draco','hagrid']

    bubbleSort(nlist_num)
    print(nlist_num)

    bubbleSort(nlist_char)
    print(nlist_char)

    bubbleSort(nlist_str)
    print(nlist_str)