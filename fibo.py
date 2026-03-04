fibo2=0
fibo1=1
fiboItself=fibo1+fibo2

def fibonacci_less_than(n):
    fibo2=0
    fibo1=1
    fiboItself=fibo1+fibo2

    print(fibo2)
    print(fibo1)
    print(fiboItself)  

    while fiboItself <= n:
        fibo2= fibo1
        fibo1= fiboItself
        fiboItself= fibo1+fibo2

        print(fiboItself)



number = int(input('fibonacci numbers until..?: '))  
fibonacci_less_than(number)    



