code='''import sys
e='57o0v1f273341506g8s9u/1E0T1/2A1I0M3N2/3D4G6K5O7R2S0/4B8CAF2H0J7L4P6QDV1X9YBZC/3YBW3U1'.split("/")
j,s,x=int,'',' '
for i in sys.argv[1]:
 if i==x: s+=x*7
 for r in e:
  if i in r:
   s+=bin(j(r[r[1:].index(i)+2],36))[2:].zfill(j(r[0])).replace("1","▄▄▄ ").replace("0","▄ ")+x*2
   break
print(s)
#'''
NULL_BYTE_BUFFER=99
print(len(code))
input()
#convert each char in code to 2 hex digits
code_hex=[hex(ord(i))[2:].zfill(2) for i in code]
for i in code_hex:
    print("i is", i, y:=int(i, 16), chr(y))
# concat hex string 
hex_2_string = "".join(code_hex)
print(hex_2_string)
# convert each 5 hex chars into unicode
unicode = [chr(int(hex_2_string[j:j+5],16)+NULL_BYTE_BUFFER) for j in range(0,len(hex_2_string),5)]

print("".join(unicode))
input()
# unicode back into hex
unicode_2_hex = "".join([hex(ord(i))[2:].zfill(5) for i in unicode])
print(unicode_2_hex)
# unicode hex back to 2-digit hex codes
s=[unicode_2_hex[i:i+2].zfill(2) for i in range(0, len(unicode_2_hex), 2)]
print(s)
input()
with open("run.py", "w") as f:
    for i in s:
        print("i is", i, y:=int(i, 16), chr(y))
        f.write(chr(int(i,16)))
import run
    
        
    
