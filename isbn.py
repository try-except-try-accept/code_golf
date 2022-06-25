import sys
for i in sys.argv[1:]:
    k=i.replace("-","")
    c=(11-(sum([(10-x)*int(k[x])for x in range(9)])%11))%11
    print(i+str(c if c!=10 else"X"))
