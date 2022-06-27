code="print('hello world')"
#convert each char in code to 2 hex digits
code_hex=[hex(ord(i))[2:].zfill(2) for i in code]
for i in code_hex:
    print("i is", i, y:=int(i, 16), chr(y))
# concat hex string 
hex_2_string = "".join(code_hex)
print(hex_2_string)
# convert each 5 hex chars into unicode
unicode = [chr(int(hex_2_string[j:j+5],16)) for j in range(0,len(hex_2_string),5)]

print(unicode)
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
    
        
    
