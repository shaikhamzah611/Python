s1= {1,2,3}
s2 = {'b','c','a'}
s3 = list(zip(s1,s2))
print(s3,"\n")

list1 = [10,20,30,40]
list2 = [400,300,200,100]

for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks = ['relaince','infosys','tcs']
price = [2750,1245,2133]

new_dict = {stocks: price for stocks,
            price in zip(stocks,price)}
print('\n{}',format(new_dict))