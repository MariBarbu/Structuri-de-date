def generator(nr_numere, max_nr):
    import random
    mylist = []
    for i in range(0,nr_numere):
        x = random.randint(1,max_nr)
        mylist.append(x)
    return mylist

def bubblesort(l):
    for i in range(1,len(l)):
        for j in range(0,len(l)-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

    return l
def countsort(l):
    f=[0]*10000000;
    for i in l:
        f[i]+=1
    l.clear()
    for i in range(0,len(f)):
        if f[i]!=0:
            for k in range(0,f[i]):
                l.append(i)
    return l

def radixsort(l):
    exista_cifre=True
    gaseste_cifra=-1
    pozitie=1

    while exista_cifre:
        exista_cifre=False
        liste=[[] for i in range(10)]
        for i in l:
            gaseste_cifra=i//pozitie
            liste[gaseste_cifra%10].append(i)
        if gaseste_cifra and pozitie>0:
            exista_cifre=True

        l.clear()
        for b in liste:
            l.extend(b)
        pozitie*=10
    return l

def mergeSort (l):
    if len(l) > 1:
        m=len(l)//2
        left=l[:m]
        right=l[m:]
        mergeSort(left)
        mergeSort(right)
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            l[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            l[k]=right[j]
            k+=1
            j+=1
    return l

def partition(l,start,end):
    leader=follower=start
    while leader<end:
        if l[leader]<=l[end]:
            l[follower],l[leader]=l[leader],l[follower]
            follower+=1
        leader+=1
    l[follower],l[end]=l[end],l[follower]
    return follower
def _quicksort(l,start,end):
    if start>=end:
        return l
    p=partition(l,start,end)
    _quicksort(l,start,p-1)
    _quicksort(l,p+1,end)
def quicksort(l):
    _quicksort(l,0,len(l)-1)
def testare(sortare,list,t1):
    t2=datetime.datetime.now()
    if list==sortare:
        print("Lista sortata in ")
        print(t2-t1)
    else:
        ok = 1
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                ok = 0
        if ok==1:
            print("Lista sortata in ")
            print(t2 - t1)
        else:
            print("Lista nesortata")

import datetime
lista=generator(10000000,1000000)
l=list(lista) #ii facem o copie lui l pentru a o sorta cu sortarea implicita
t1=datetime.datetime.now()
l.sort()
t2=datetime.datetime.now()
print("Functia sort: ")
print(t2-t1)
l=list(lista)
print("Mergesort: ")
t1=datetime.datetime.now()
testare(mergeSort(l),list,t1)
l=list(lista)
print("Quicksort:")
t1=datetime.datetime.now()
testare(quicksort(l),list,t1)
l=list(lista)
print("Radixsort: ")
t1=datetime.datetime.now()
testare(radixsort(l),list,t1)
l=list(lista)
print("Countsort:")
t1=datetime.datetime.now()
testare(countsort(l),list,t1)
l=list(lista)
print("Bubblesort:")
if len(l)<=10000:
    t1=datetime.datetime.now()
    testare(bubblesort(l),list,t2)
else:
    print("Prea multe numere pentru bubble")






