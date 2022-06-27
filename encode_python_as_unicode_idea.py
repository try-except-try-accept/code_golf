code="print('hello world')"
code_hex=[hex(ord(i))[2:].zfill(2) for i in code]
for i in code_hex:
    print("i is", i, y:=int(i, 16), chr(y))
x = [code_hex[j:j+5] for j in range(0,len(code_hex),5)]
s="".join(hex(ord(i))[2:]for i in x)
s=[s[i:i+2] for i in range(0, len(s), 2)]
with open("run.py", "w") as f:
    for i in s:
        print("i is", i, y:=int(i, 16), chr(y))
        f.write(chr(int(i,16)))
import run
    
        
    
