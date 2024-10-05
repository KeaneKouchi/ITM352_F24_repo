#Debugging exercise # 5

# relied heavily on ChatGPT because I'm not really sure what 
# fibonacci is 
#
def fibonacci(n):
    # used a known sequence for fibonacci
    fib_sequence = []
    a, b = 0, 1
    for num in myList:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# altered the ChatGPT code to use the list given in the original code
myList = [1, 2, 3, 4, 5]
print(fibonacci(myList))
