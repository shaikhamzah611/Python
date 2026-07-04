tup1 = (4, 3, 2, -1, 18)
tup2 = (2, 4, 8, 3, 2, 9)

products = []

min_length = min(len(tup1), len(tup2))

for i in range(min_length):
    product = tup1[i] * tup2[i]
    products.append(product) 
    
result_tuple = tuple(products)

print("Tuple 1:", tup1)
print("Tuple 2:", tup2)
print("Element-wise product tuple:", result_tuple)