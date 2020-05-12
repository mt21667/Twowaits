''' 1st question'''
a='Hello World'
print(a[::-1])

'''2nd Question'''
x="hello"
result=[]
def permute(x,i,length):
    if length==i:
        result.append(''.join(x))
    else:
        for j in range(i,length):
            x[i],x[j]=x[j],x[i]
            permute(x,i+1,len(x))
            x[i],x[j]=x[j],x[i]
permute(list(x),0,len(x))
print(str(result))
#inbuilt function
from itertools import permutations    
print([''.join(i) for i in permutations(x)])

'''3rd Question'''
a="My name is manish tiwari"
def remove_duplicate(a,n):
    index=0
    for i in range(0,n):
        for j in range(0,i+1):
            if(a[i]==a[j]):
                break
        if(j==i):
            a[index]=a[i]
            index=index+1
    return ''.join(a[:index])
n=len(a)
print(remove_duplicate(list(a),n))
 
'''4th question'''
l=[12,1,4,12,14,13,22,4,2,1]
def remove(a):
    result=[]
    for i in a:
        if i not in result:
            result.append(i)
    return result
print(remove(l))

'''5th question'''
l=[12,1,4,14,13,22,4,2]
m=[1,2,3,4,13,12]
def intersect(l,m):
    res=[value for value in l if value in m ]
    return res
print(intersect(l,m))


