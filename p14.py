def fib(n):
    a,b=0,1
    while b<n:
      print(b,end=" ")
    a,b=b,a+b
num=int(input("Enter any number to print Fibonacci series"))
fibonacci.fib(num)
