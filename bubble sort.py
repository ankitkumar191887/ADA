import random
a = []
n=int(input("Enter n:"))
for i in range(0,n):
    n = random.randint(1,50)
    a.append(n)
print(a)


 
for i in range(0,len(a)-1): 
        for j in range(len(a)-1): 
            if(a[j]>a[j+1]): 
                temp = a[j] 
                a[j] = a[j+1] 
                a[j+1] = temp 

print(a)
