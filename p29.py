# Problem 29 - 31/01/2021
# This isn't my code, I kinda know how it works
# I thought about this but I didn't know how to implement the first part
n=int(input())

k=1
while(pow(2,k)<=n):
    k+=1
last=k

lists={}
for i in range(1,last):
    if i != 1:
        lists[i]=lists[i-1].copy()
    else:
        lists[i]=[]
    for j in range(2,n+1):
        lists[i].append(j*i)
    if(i!=1):
        temp=list(set().union(lists[i-1],lists[i]))      
        lists[i]=temp

check=[0] * (n-1)
ans=0
for i in range(2,n+1):
    if(check[i-2]==0):
        check[i-2]=1
        j=i*i
        while(j<=n):
            check[j-2]=1
            j=j*i
        
        k=1
        while(pow(i,k)<=n):
            k+=1
        last=k
        ans+=len(lists[k-1])

print(ans)
