from itertools import permutations
a=''.join
I=int
for i in range(1000,939659):
 j=str(i)
 L=len(j)
 if L%2!=0: continue
 for s in permutations(j,L):
  m=len(s)//2
  x,y=I(a(s[:m])),I(a(s[m:]))   
  if i==x*y:
   print(i)
   break
