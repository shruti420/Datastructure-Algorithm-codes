# Uses python3
import sys

def optimal_sequence(m):
    a=[0,0]
    for i in range(2,m+1):
        if i%3==0 and i%2==0:
            a.append(min(a[i//2],a[i//3],a[i-1])+1)
        elif i%3==0:
            a.append(min(a[i//3],a[i-1])+1)
        elif i%2==0:
            a.append(min(a[i//2],a[i-1])+1)
        else:
            a.append((a[i-1])+1)
    return backtrack(a,m)
def backtrack(a,m):
    result=[]
    result.append(m)
    current = m
    for i in range(a[-1],0,-1):
        if current%3==0 and a[current//3]==(i-1):
            current=current//3
            result.append(current)
        elif current%2==0 and a[current//2]==(i-1):
            current = current//2
            result.append(current)
        elif a[current-1]==(i-1):
            current = current-1
            result.append(current)
    return result

n = int(input())
if n == 1:
    print(0)
    print(1)
    sys.exit(0)

a= (optimal_sequence(n))
print(len(a)-1)
for x in reversed(a):
    print(x,end=" ")
