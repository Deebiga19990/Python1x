# Exception
# abnormal event during the execution program, But ut can handled

# Error - specific code ->  1 gb -> 1.2 gb ? StackOverFlow
# 10 , 12 - Error -> It very diffcult to overcome
# MemoryError - Error -> Restart, retry

# Java -> Python

print("Insert the Card")

try:
    a = int(input("Enter your A number"))
    b = int(input("Enter your B number"))
    c=a/b
    print(c)
except Exception as e:
    print("XX Error due to number/0")

print("Take the Card")