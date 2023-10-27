#counting vowels and consonants
string_name=input("Enter the string\n")
vowel=0
consonant=0
for ch in range(0,len(string_name)):
    string_name=string_name.lower()
    if((string_name[ch]=='a') or (string_name[ch]=='e') or (string_name[ch]=='i')
            or (string_name[ch]=='o') or (string_name[ch]=='u')):
        vowel+=1
    elif(string_name[ch]== " "):
        pass
    else:
        consonant+=1

print(f"The number of vowels in the given string is {vowel}")
print(f"The number of consonant in the given string is {consonant}")
