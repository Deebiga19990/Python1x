my_dict = {'a': 1, 'b': 2}

val = my_dict.pop('a')
print(val)

print(my_dict)

# API Testing -> JSON so we can use Dict which is similar data type as JSON

print(dir(dict()))
print(dir(list()))

# How to Iterate over the Dict?

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
print(len(knights))

for k,v in knights.items():
    print(k,v)

for k, v in knights.items():
    print(k)
    print(v)

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)
val = my_dict.popitem()
print(val)
print(my_dict)

del my_dict

#print(my_dict)