def reverse_string(input_str):
    reverse_str=""
    for ch in input_str:
        reverse_str=ch+reverse_str
    return reverse_str

input_str="ABCD"
print(reverse_string(input_str))