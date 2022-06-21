'''99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.

98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.

…

1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.'''

o=" of beer"
a="bottle"+o
a2="bottles"+o
b='on the wall.'
#x
b
c='Take one down and pass it around,'
#x
a2+b[:-1]+"."
#x
a2
b
#x
a2+"."
nm="no more"
g='Go to the store and buy some more'
s=str
for x in range(99, -1,-1):
    nx=x-1
    if x==0:
        x,c,nx=nm,g,99
    x=nm if x==0 else x
    
    print(x,a if x==1 else a2,b[:-1]+',',x,a+'.',c,end=" ")
    print(nx,a if nx==1 else a2,b)

