phone_book = {"Batman": 987654321, "Superman": 1234567890, "Wonder": 97876545}

# Dict ?  It is very close to the JSON
print(phone_book)
print(type(phone_book))
print(len(phone_book))

print(phone_book["Batman"])
print(phone_book["Wonder"])

# You can access element by Key only - Dict


phone_book2 = dict(Batman=123, Cersei=342, GB=323)
print(phone_book2)
print(type(phone_book2))
print(phone_book2['GB'])
print(phone_book2["GB"])
print(phone_book2.get('GB'))
print(phone_book2.get("GB"))

pramod_details = dict(name="Pramod", age=34, isMale=True, Address="KA")
pramod_details2 = {"name": "Pramod", "age": 34.34, "isMale": True, "Address": "KA"}
print(pramod_details)
print(pramod_details['age'])
print(pramod_details.get('age'))
print(pramod_details2['age'])



print(pramod_details)

#it takes keys as intergers but better to make keys string always
pramod_details3 = {"name": "Pramod", 21: 34.34, 56: True, "Address": "KA"}
print(pramod_details3.get(56))