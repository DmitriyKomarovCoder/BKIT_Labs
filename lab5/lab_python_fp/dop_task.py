list1 = [1,2, 3]
print([(i, i * i) for i in list1])
print(list(map(lambda i: (i, i*i), list1)))
print(list((x,y) for ix, x in enumerate(list1) for iy, y in enumerate(map(lambda x: x**2, list1)) if ix == iy))
print(list(zip(list1, map(lambda i: i*i, list1))))