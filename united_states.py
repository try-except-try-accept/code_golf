import sys

s='''Alabama	AL
Alaska	AK
Arizona	AZ
Arkansas	AR
California	CA
Colorado	CO
Connecticut	CT
Delaware	DE
District of Columbia	DC
Florida	FL
Georgia	GA
Hawaii	HI
Idaho	ID
Illinois	IL
Indiana	IN
Iowa	IA
Kansas	KS
Kentucky	KY
Louisiana	LA
Maine	ME
Maryland	MD
Massachusetts	MA
Michigan	MI
Minnesota	MN
Mississippi	MS
Missouri	MO
Montana	MT
Nebraska	NE
Nevada	NV
New Hampshire	NH
New Jersey	NJ
New Mexico	NM
New York	NY
North Carolina	NC
North Dakota	ND
Ohio	OH
Oklahoma	OK
Oregon	OR
Pennsylvania	PA
Rhode Island	RI
South Carolina	SC
South Dakota	SD
Tennessee	TN
Texas	TX
Utah	UT
Vermont	VT
Virginia	VA
Washington	WA
West Virginia	WV
Wisconsin	WI
Wyoming	WY'''.split("\n")
c = 0
s={i.split('\t')[0]:i.split('\t')[1] for i in s}
s2=dict(s)
h = []


def category_approach():

    config={"first_last":"",
            "initials":"",
            "first_two":"",
            "misc":""}
    f={}
    for n,a in s.items():
        x = sum(ord(i) for i in n)*ord(n[0])
        if x in h:
            input("clash")
        h.append(x)
        
        if n[0]+n[-1].upper() == a:
            print(n)
            label = "first_last"
        elif " " in n and n.split(" ")[0][0]+n.split(" ")[-1][0] == a:
            print(n)
            label = "initials"
        elif n[:2].upper() == a:
            print(n)
            label = "first_two"
        else:
            label = "misc"
            x = chr(x)+chr(int(str(ord(a[0]))+str(ord(a[1]))))


        config[label]+=chr(x) if type(x) == int else x

    return config

for n, a in s.items():
    x = chr(sum(ord(i) for i in n)*ord(n[0]))
    a = chr(int(str(ord(a[0]))+str(ord(a[1]))))
    print(x+a,end="")

input()

def solution(): 
   s="꩟ᦰ閍᦯럔ᦾ퀴ᦶ𐧨ᩭ홙᩻𒴽᪀헔᫕🿜᫓샆ᮤ슲᯽Ꝙᱩ詍᳈᳐암᳒爐᳅뉫ᶟᶥ𑓼ᷱ鍢ṙṘ𚁈ṕṝ𑭖Ṣ𖌹ṧ𐉟ṣퟶṨẽ됒Ỏ𗾚Ề𒍈Ể𑽒ễố𙾘ẻ𕺲Ẽ笡ἤ杖ἧ뺶Ἦ𘶀ᾁ𖫪⁑𛳔₯𗟅₰𓏈℞ꦤℨ蕺ↈ﫲⇬𑔦⇙𖞎∽𛆤≒𔔻≅ﶆ≕"
    
    for a in sys.argv[1:]:
     i=s[s.index(chr(sum(ord(i)for i in a)*ord(a[0])))+1]
     print(chr(ord(i)//100)+chr(ord(i)%100))


class sys:
    argv=[None] + '''Washington
Connecticut
Alaska
Alabama'''.split("\n")
solution()
