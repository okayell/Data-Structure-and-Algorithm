
#  一個一個拿出來比, 把最小的擺置最左邊
print("---------- Selection Sort ----------")
print("Time Complexity:")
print(" Best: n^2\n  Avg: n^2\nWorst: n^2\n")
s = [92,32,16,22,48,76,61,0,71]
print("Before:\n",s)
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        if s[i] > s[j]:
            s[i],s[j] = s[j],s[i]
print("After:\n",s)
print("\n")


#  倆倆互換, 把最大的擺置最右邊
print("---------- Bubble Sort ----------")
print("Time Complexity:")
print(" Best: n\n  Avg: n^2\nWorst: n^2\n")
s = [92,32,16,22,48,76,61,0,71]
print("Before:\n",s)
for i in range(1,len(s)):
    for j in range(0,len(s)-i):
        if s[j] > s[j+1]:
            s[j],s[j+1] = s[j+1],s[j]
print("After:\n",s)      
print("\n")


#  從最左兩個數開始排序, 再逐次加入下一個數進行排序
print("---------- Insertion Sort ----------") 
print("Time Complexity:")
print(" Best: n\n  Avg: n^2\nWorst: n^2\n")    
s = [92,32,16,22,48,76,61,0,71]
print("Before:\n",s)
for i in range(1,len(s)):
    tmp = s[i]
    j = i-1
    while ( j >= 0 and tmp < s[j] ):
        s[j], s[j+1] = s[j+1], s[j]
        j = j - 1
print("After:\n",s)      
print("\n")


#  
print("---------- Quick Sort ----------") 
print("Time Complexity:")
print(" Best: nlogn\n  Avg: nlogn\nWorst: n^2\n")    
s = [92,32,16,22,48,76,61,0,71]
print("Before:\n",s)

print("After:\n",s)  
print("\n")



            