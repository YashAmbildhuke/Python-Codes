def print_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    
n=int(input("Enter the numeber :- "))
print_fact(n)