p=print
def f(a,b):
 b,a=a,a+b
 p(a)
 if a!=832040:
   f(a,b)
p(0)
f(0,1)
