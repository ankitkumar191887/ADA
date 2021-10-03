import random
a = []
n=int(input("Enter n: "))
for i in range(0,n):
    n = random.randint(1,50)
    a.append(n)
print(a)

def mergeSort(a):
    if len(a) > 1:
        r = len(a)//2
        L = a[:r]
        M = a[r:]
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
               a[k] = L[i]
               i += 1
        else:
              a[k] = M[j]
              j += 1
              k += 1
        while i < len(L):
                    a[k] = L[i]
                    i += 1
                    k += 1
        while j < len(M):
                    a[k] = M[j]
                    j += 1
                    k += 1
                    mergeSort(a)

print("Sorted array is: ")
print(a)
