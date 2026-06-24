L = [3,45,7,39,97,65,201]
print("Original List:",L)

count = 0 

for  i in L:
    count +=i

avg = count/len(L)

print("Sum=",count)
print("Average=",avg)

L.sort()

print("Smallest element is:",L[0])
print("Largest element is:",L[-1])