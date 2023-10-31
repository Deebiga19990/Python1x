# Remove a key-value pair from the dictionary.
my_dict=dict(a='1',b='2',c='3',d='4')
print("My dictionary:",my_dict)
key_to_remove= input("Enter the key to be removed\n")
my_dict.pop(key_to_remove)
print(f"My dictionary after removing a key_value pair {my_dict}")
my_dict2= dict(name="Ross", age="23", is_male=False,Address="Vellore",pincode="632009",Ph="123456" )
my_dict2.pop("pincode")
print("Dictionary after popping pin_code:", my_dict2)