I,L,r,a,s=int,len,range,''.join,"𰌃𓈶𰌃ㄳ𹍓〱𴌳񓀰𱍓𳀰𰌓򃈷𰌃𣄸𷌃㘸𸌃𓀲𵌓㄰𴌣񣀱𰍓𣄰𱌃񓈶𴌓㔷𵌃𓀸𱌳񓄱𰍳񓠱𱍓񣜲𱌓񣜲𵌓𓜰𶍳𓄸𴍃ㄲ𰍣〱𲌳𳔴𱌣񃐸𳌓𣔲𴎃𓈵𴌳𳄲𵍃񣀱𲍓񓀰𱌣񣀲𷌓𣘸𴍣𓈹𶍃ㄲ𹍳񳔱𳌓𣐲𱌳𣐳𰌓𳌲𴍓𓌴𷌣񓄳𵎃𣠱𳍓򃌷𱌳񣔲𵌓𳘹𴎃𓐰𳍓ㄴ𵌳𓐱𴍣𓌷𱍃񣤵𲌓񓀳𰌃𓔲𶌃򃄵𲍣򃔱𵌳񃌶𱍓񣈴𰌓񓘲𸎓𓔶𹌓񓄶𲎓񳘱𶌳򓐴𱍳𣠲𲌓񳌲𵌃𓜴𳍳ㄷ𵌳𣤱𸌃𣈵𱎃㈹𷌓򃈲𵌃𓠲𶍓ㄸ𶍣𣐱𹌃𣘰𱎓𣄵𰌓򓌲𵍳𓤳𹍃񓄹𷍳𣔲𰌓򃔲𲌃񓜸𵌣𓄸𹍣𣄳𴍣񣈱𵎃񣀲𱍣񳌳𲌓񳘳𸌣𓠴𸎃𣈶𴎓򃈲𶎃񳈲𲎓񣐸𲌳𳠹𶌣񃄵𶍃𣐵𱎃𣈵𱎃򓘲𵌳񳔰𲍓񃜴𰌣񣀳𳎃𣘲𹎃񃈶𳌃񳐲𸍃񓤸𲎃񃜶𰌣򃘴𱍣𣤶𳌣㌰𴍳𓜳𱌣񃜵𳌓𣤷𵌳𓔵𹍃𳄵𹌃㌱𹌃񓤳𱎓񓌶𳌣񣐵𲌳𣤳𴍣𳈹𶍓񣌳𶍓񓀳𳍣򓘰𳌳򃈹𶌳񃄶𵌳𳐶𹍣򃌶𱎓򃤳𶌣򓤲𳍣񓘳𸌳񣠵𵌃𳘹𱎃򓌷𱎃򓌳𷎃񃀰𳍳򃐱𸌳񳠴𵌃𳠴𹌓𣌸𶍃𓔳𹌣񓘶𴌃񃤶𸍃𓐸𹍓񃄶𶍓㐱𶎓򃠴𲎃򓠰𴌣򓘶𴍃񃜹𱍣񃔶𸍃㐵𷍣〴𵎃񣐰𴍳񓌸𰍃򃘷𲌃񃠹𱍓򓐸𹎓񓔴𹎃񓔰𵌓񣠷𹍓𣤶𷌣񓌶𵌳򓔳𸍣񓀵𵎓𓠸𵍣񳘴𸍓񣠷𵌃񣈹𶎃㘳𸎓񓀶𷌳򓈰𶍳򓔰𰍳𣤶𸎃񳌶𶎓񓜳𸍃񣠷𶎓񳤲𷎃򓈵𰍳򃤵𲍓񳤲𵎃񓜹𴌃򃠸𰎓򓄹𸌃򓤶𴎃𓔹𵎃򃈹𶎓񣠴𱎓򓔹𳎓񣔸"
i=a([hex(ord(u))[2:].zfill(5)for u in s])
a=a([chr(I(i[j:j+2], 16))for j in r(0,L(i),2)])
for i in r(0, L(a), 6):
 print(I(a[i:i+6]))
