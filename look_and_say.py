from collections import Counter
i="111221"
for j in range(20):
 c=0
 L=0
 s=""
 for n in i:
  if L!=0 and n!=L:
   s+=f"{c}{L}"
   c=1
  else:
   c+=1
  L=n
 s+=f"{c}{L}"
 print(i:=s)
 input()
