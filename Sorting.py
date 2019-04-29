import numpy as np
import pandas as pd
import time

def timeCount(fun):
    start = time.perf_counter()
    fun
    end = time.perf_counter()
    elapsed = end - start
    return elapsed*10**6

def bubbleSort(lst):    #  倆倆互換, 把最大的擺至最右邊
    for i in range(1,len(lst)):
        for j in range(0,len(lst)-i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst

def selectionSort(lst):    #  一個一個拿出來比, 把最小的擺置最左邊
    for i in range(0,len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j],lst[i] 
    return lst

def insertionSort(lst):    #  從最左兩個數開始排序, 再逐次加入下一個數進行排序
    for i in range(1,len(lst)):
        tmp = lst[i]
        j = i-1
        while ( j >= 0 and tmp < lst[j] ):
            lst[j], lst[j+1] = lst[j+1], lst[j]
            j = j - 1
    return lst

def quickSort(lst):    #  設定基準, 分割成:小於基準值+基準值+大於基準值, 進行遞迴
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

lst = np.random.randint(0,1000,5000)
#print("List:",lst)

print("1. Bubble sort:")
#print(bubbleSort(lst))
t1 = timeCount(bubbleSort(lst))
print("  Running time:", t1, "(us)")
print("  Time Complexity:",end="")
print(" Best: n\n\t\t    Avg: n^2\n\t\t  Worst: n^2\n")

print("2. Selection sort:")
#print(selectionSort(lst))
t2 = timeCount(selectionSort(lst))
print("  Running time:", t2, "(us)")
print("  Time Complexity:",end="")
print(" Best: n^2\n\t\t    Avg: n^2\n\t\t  Worst: n^2\n")

print("3. Insertion sort:")
#print(insertionSort(lst))
t3 = timeCount(insertionSort(lst))
print("  Running time:", t3, "(us)")
print("  Time Complexity:",end="")
print(" Best: n\n\t\t    Avg: n^2\n\t\t  Worst: n^2\n")

print("4. Quick sort:")
#print(quickSort(lst))
t4 = timeCount(quickSort(lst))
print("  Running time:", t4, "(us)")
print("  Time Complexity:",end="")
print(" Best: n log n\n\t\t    Avg: n log n\n\t\t  Worst: n^2\n")

df = pd.DataFrame([t1,t2,t3,t4],index=["Bubble","Selection","Insertion","Quick"],columns=["Time(us)"])
print(df)