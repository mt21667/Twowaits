'''1st Question'''
num=int(input("Enter the number to check:\n"))

def check_even_odd(num):
    if (num%2==0):
        print("the given number ",num," is even")
    else:
        print("the given number ",num," is odd")
check_even_odd(num)

def check_prime(num):
    if num>1:
        for i in range(2,num//2):
            if(num%i)==0:
                print("number is not prime")
                break
        else:
            print("number is prime")
    else:
        print("Number is not prime")
check_prime(num)

'''Pallindrome Number'''
def check_pallindrome(num):
    temp=num
    sum=0
    while num>0:
        r=num%10
        sum=(sum*10)+r
        num=int(num/10)
    if(temp==sum):
        print("number is pallindrome")
    else:
        print("number is not pallindrome")
check_pallindrome(num)

'''ARMSTRONG NUMBER'''
def order(n):
    x=0
    while(n>0):
        x=x+1
        n=int(n/10)
    return x
def armstrong(n):
    temp=n
    x=order(n)
    sum=0
    while(n>0):
        a=n%10
        sum=sum+pow(a,x)
        n=int(n/10)
    if(sum==temp):
        print("no is armstrong")
    else:
        print("No is not armstrong")
armstrong(num)


'''2nd Question'''
num=int(input("Enter the number of terms\n"))
def fibo(n):
    if n<=1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
def show_fibo(num):
    print("the fibo series of ",num," numbers is:")
    for i in range(num):
        print(fibo(i))
show_fibo(num)

'''3rd question'''
def up_pattern(n):
    s=2*n-2
    for i in range(0,n):
        for j in range(0,i):
            print(end=" ")
        print("*",end='')
        for k in range(s):
            print(end=' ')
        s=s-2
        print('*',end='')
        print('\r')
def low_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(end=' ')
        print('*',end='')
        for j in range(2*i):
            print(end=' ')
        print('*',end='')
        print('\r')
def  complete_pattern(n):
    up_pattern(n)
    low_pattern(n)

complete_pattern(4)

'''4th question'''
def upPattern(n):
    for i in range(n):
        for j in range(i,n):
            print('* ',end='')
        for m in range(0,4*i+1):
            print(end=' ')
        for p in range(i,n):
            print('* ',end='')
        print('\r')

def lowPattern(n):
    s=4*n-3
    for i in range(n):
        for j in range(i+1):
            print('* ',end='')
        for k in range(s):
            print(end=' ')
        s=s-4
        for m in range(i+1):
            print('* ',end='')
        print('\r')

def comPattern(n):
    upPattern(n)
    lowPattern(n)

comPattern(5)

'''5th question'''
def up(n):
    for i in range(n):
        for j in range(1,2*n):
            if j%2==1:
                print(n,end='')
            else:
                print('*',end='')
        n=n-1
        print('\r')
def low(n):
    for i in range(n):
        for j in range(1,2*i+2):
            if j%2==1:
                print(i+1,end='')
            else:
                print('*',end='')
        print('\r')
def full(n):
    up(n)
    low(n)
full(5)
    
    




