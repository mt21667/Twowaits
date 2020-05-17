# -*- coding: utf-8 -*-
"""
@author: Manish Tiwari
"""

'''1st question'''
def convert(num):   
    temp=num
    sum=0
    count=1
    if temp==0:
        return 5
    while temp>0:
        if temp%10==0:
            sum+=(5*count)
        count*=10
        temp=int(temp/10)
    return num+sum

num=int(input('enter the number'))
convert(num)

'2nd question'

def greatest(arr):
    n=len(arr)
    maxi=arr[n-1]
    arr[n-1]=-1
    for i in range(n-2,-1,-1):
        temp=arr[i]
        arr[i]=maxi
        if temp>maxi:
            maxi=temp
        
arr=[5,4,3,2,1]
greatest(arr)

'''3rd question'''

def maxi(arr):
    n=len(arr)
    if n==0:
        return 0
    if n==1:
        return arr[0]
    if n==2:
        return max(arr)
    dp=[0]*n
    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])
    for i in range(2,n):
        dp[i]=max(dp[i-2]+arr[i],dp[i-1])
    return dp[n-1]
arr=[5,2,3,6,4,7,6,8]
print("the maximum amount stolen by thief is :",maxi(arr))
        
'''4th problem '''

weight_arr=[2,3,4]
profit_arr=[1,2,5]
n=len(weight_arr)
Max_weight=6
def knapsack(weight_arr,profit_arr,Max_weight,n):
    if n==0 or Max_weight==0:
        return 0
    if weight_arr[n-1]>Max_weight:
        return knapsack(weight_arr,profit_arr,Max_weight,n-1)
    else:
        return max(profit_arr[n-1]+knapsack(weight_arr,profit_arr,Max_weight-weight_arr[n-1],n-1),knapsack(weight_arr,profit_arr,Max_weight,n-1))
knapsack(weight_arr,profit_arr,Max_weight,n)

#using dynamic programmming
def knapsack1(weight,profit,W,n):
    if n==0 or W==0:
        return 0
    dp=[[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif weight[i-1]<=j:
                dp[i][j]=max(profit[i-1]+dp[i-1][j-weight[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][W]
profit=[6,1,15]
weight=[1,3,4]
W=7
knapsack1(weight,profit,W,n)

'''5th question'''
def double_sort(arr):
    n=len(arr)
    left=0
    right=n-1
    k=0
    while(left<right):
        while(arr[left]%2!=0):
            left+=1
            k+=1
        while(arr[right]%2==0 and left<right):
            right-=1
        if (left<right):
            arr[left],arr[right]=arr[right],arr[left]
    odd=arr[:k]
    even=arr[k:]
    odd.sort(reverse=True)
    even.sort()
    odd.extend(even)
    return odd
arr=[1,3,2,7,5,4]
result=double_sort(arr)
for i in result:
    print(str(i)+" ")
