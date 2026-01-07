# Recursion means, a function is calling itself

def fact(n):
    if n==1 or n==0: return 1
    else:
        return n * fact(n-1)
    
print(f"The factorial of 5 is: {fact(5)}")


'''
    Fibonacci series: 0 1 1 2 3 5 8 13 21 34 ...
             indeces: 0 1 2 3 4 5 6 7  8  9 ...
             
    fib(0) = 0
    fib(1) = 1
    fib(2) = fib(0) + fib(1)
    fib(3) = fib(1) + fib(2)
    fib(4) = fib(2) + fib(3)
    fib(5) = fib(3) + fib(4)
    .................
    .................
    .................
    fib(n) = fib(n-2) + fib(n-1)
''' 

fib = lambda x : x if x<=1  else fib(x-2) + fib(x-1) 
'''
    or,
def fib(x):
    if(x<=1): return x
    else: return fib(x-2) + fib(x-1)
'''
for i in range(10):
    print(fib(i),end="  ")
