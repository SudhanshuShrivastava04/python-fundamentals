n = int(input("Enter value of n: "))

def fibonacci(n):
    print(f"\nFibonacci Series for N = {n}\n")
    a = 0
    b = 1 

    while(a < n):
        print(a, end=" ")
        a, b = b, a + b 
    
    print()

def first_n_element(n):
    print(f"\nFirst {n} Elements in Fibonacci Series\n")
    a = 0
    b = 1 

    while(n > 0):
        print(a, end=" ")
        a, b = b, a + b 
        n -= 1
    
    print()

fibonacci(n)
first_n_element(n)