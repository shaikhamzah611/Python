class pair():
    def twosum(Self,num,target):
        lookup = {}

        for i,num in enumerate(num):
            if target - num in lookup:
                return (lookup[target-num],i)
            lookup[num]=i
val = int(input("Enter the sum for which you want to search up: "))
print("index1 = %d,index2 = %d"% pair().twosum((10,20,30,40,50,60,70,80,90),val))