'''1st question'''

def Count_occurences(tup,n):
    count=0
    for i in range(len(tup)):
        if tup[i]==n:
            count+=1
    return count
x=int(input("enter the total no of elements in list"))
tup=[]
print('Enter the elements one by one')
for i in range(x):
    tup.append(int(input()))
n=int(input("enter the element to count its occurence"))
print(n,"occured ",Count_occurences(tuple(tup),n)," times in this tuple")

'''2nd question'''
test_list = [(3,2,1), (4,2,7), (3,2,1), (5,8,4)] 
n = int(input("enter the index to which sorting perform"))
test_list.sort(key = lambda x: x[n])
print("The original list is : ",(test_list)) 
print("List after sorting tuple by Nth index sort : ",test_list) 

'''3rd qyestion'''
dictionary={"student1":20,'student 2':22,'student 3':21,'student 4':43}
max1=max(dictionary.values())
max2=0
for i in dictionary:
    if dictionary[i]>max2 and dictionary[i]<max1:
        max2=dictionary[i]
print("second maximum value in dictionary is:",max2)

#2nd method
max2=sorted(dictionary.values())[-2]
print("second maximum value in dictionary is:",max2)

'''4th question'''
dictionary1={"student1":20,'student 2':20,'student 3':21,'student 4':43,"student 5":22,
             'student 6':20,'student 7':21,'student 8':20}
dict=dictionary1.copy()
print("original dictionary",dictionary1)
values=[]
for i in dict:
    if dictionary1[i] in values:
        dictionary1.pop(i)
    else:
        values.append(dictionary1[i])
print("dictionary after removing duplicate values",dictionary1)


'''5th question'''
n= int(input("Enter the no of votes: "))
Votes = []
for i in range(n):
    Votes.append(input("Enter the name of the Candidate to cast the Vote: "))

vote = set(Votes)
Vote = list()

for name in Votes:
    Vote.append((name, Votes.count(name)))  
Vote.sort(key = lambda x : x[0], reverse = True )
Vote.sort(key = lambda x : x[1])

print(" Candidate who won the election is",Vote[-1][0])
