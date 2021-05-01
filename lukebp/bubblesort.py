def bubblesort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i] > nlist[i+1]:
                nlist[i],nlist[i+1] = nlist[i+1],nlist[i]


def bubble():
    nlist_num = [74, 11, 8, 28, 24, 66, 84]

    bubblesort(nlist_num)
    print(nlist_num)




