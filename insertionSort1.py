#!/bin/python
def insertionSort(ar): 
    shiftV = ar[len(ar)-1]
    i = len(ar)-1
    while i>0:
        if(ar[i-1]>shiftV):
            ar[i]=ar[i-1]
        else: 
            ar[i] = shiftV
            break
        print ' '.join(map(str,ar))
        i=i-1
    if(i==0): ar[i] = shiftV
    print ' '.join(map(str,ar))   
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
