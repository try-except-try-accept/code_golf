t=["   *","  ***"," *****","   *"]
for i in range(7):
    print("\n".join(t)+"\n")
    (t := [" "+j for j in t]).insert(-1," *"+t[-2].strip()+"*")
