
# attempt 1 - 407th
t=["   *","  ***"," *****","   *"]
for i in range(7):
    print("\n".join(t)+"\n")
    (t := [" "+j for j in t]).insert(-1," *"+t[-2].strip()+"*")

# attempt 2 - 352nd
r,p=range,print
for i in r(3,10):
    for j in r(i):
        p((" "*(i-j))+("*"*((j*2)+1)))
    p((" "*i)+"*\n")

