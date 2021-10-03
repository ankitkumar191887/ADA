import random
a = []
n=int(input("Enter n:"))
for i in range(0,n):
    n = random.randint(1,50)
    a.append(n)
print(a) 



for i in range(1, len(a)): 
        temp = a[i] 
        j = i-1 
        while j >= 0 and temp < a[j] : 
                a[j + 1] = a[j] 
                j = j-1 
        a[j + 1] = temp 

print(a)
