
import sys


class sys:
    argv = [None,"NYMPH FOR 1057283694 QUICK BUD JIGS AJZLRCPUGIMENQWKHFTDVSOYXB WALTZ VEX"]



e='''57o0v1f273341506g8s9u/1E0T1/2A1I0M3N2/3D4G6K5O7R2S0/4B8CAF2H0J7L4P6QDV1X9YBZC/3YBW3U1'''.split("/")
j,s,x=int,'',' '
for i in sys.argv[1]:
    if i==x: s+=x*7
    for r in e:
        if i in r:           
            s+=bin(j(r[r[1:].index(i)+2],36))[2:].zfill(j(r[0])).replace("1","▄▄▄ ").replace("0","▄ ")+x*2
            break
print(s)



e='57o0v1f273341506g8s9u/1E0T1/2A1I0M3N2/3D4G6K5O7R2S0/4B8CAF2H0J7L4P6QDV1X9YBZC/3YBW3U1'.split("/")
j,s,x=int,'',' '
for i in sys.argv[1]:
    if i==x: s+=x*7
    for r in e:
        if i in r:
            s+=bin(j(r[r[1:].index(i)+2],36))[2:].zfill(j(r[0])).replace("1","▄▄▄ ").replace("0","▄ ")+x*2
            break
print(s)
