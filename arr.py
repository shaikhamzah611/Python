import array as arr

array_num = arr.array("i",[1,3,4,5,6,3,9,3])
print("The Original "+str(array_num))
print("The Number of occurence of 3 is: "+str(array_num.count(3)))

array_num.reverse()
print("The Reverse Order is: ")
print(str(array_num))