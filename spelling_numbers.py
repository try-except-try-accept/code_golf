

class sys:
 argv=[None] + list(map(str, range(1, 1001)))


#import sys
m={0:['','','ten'],
1:['one','x','eleven'],
2:['two','twen','twelve'],
3:['three','thir'],
4:['four','for'],
5:['five','fif'],
6:['six']*2,
7:['seven']*2,
8:['eight','eigh'],
9:['nine']*2}
p=print
for a in sys.argv[1:]:
 try:
  p({'0':'zero','1000':'one thousand'}[a])
  continue
 except:
  1   
 t=""if"00"in a else" and "
 a,i,y=list(a.zfill(3)),0,[]
 while a:
  x=int(a.pop(0))
  s,j="",m[x]
  y+=[j[i]if len(a)>0 else x]
  i=(i+1)%len(j)  
 r=m[y[-1]][0]
 d=y[-1]
 if y[0]:
  y[0]+=" hundred"+t 
 if y[1]=="x":
  y[1]=m[d][-1].replace("fo","fou")
  r="teen"if d>2 else""
 elif y[1]!="":
  y[1]+="ty"+(""if y[-1]==0 else"-")
 y[-1]=r
 f="".join(y)
 f=f.replace("  "," s")
 p(f)
