#using python3
def fibonacci_sum(n):

    if n < 2: print(n)
    else:
        a, b = 0, 1
        sum=1
        for i in range(1,n):
            a, b = b, (a+b)
            sum=sum+b
    lastdigit=(sum)%10
    print(lastdigit)


n = int(input(""));
fibonacci_sum(n);
