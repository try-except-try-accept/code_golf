p,s,n=print,[0],0
for i in range(1,1001):
 p(n)
 j=i-2
 while j!=-1 and s[j]!=n:
  j-=1
 s+=[i-j-1 if j!=-1 else 0]
 n=s[i]
