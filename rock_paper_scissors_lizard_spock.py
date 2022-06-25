import sys

class sys:
    argv = [None] + '''🦎🖖
🦎💎
💎💎
🖖🦎
📄💎
🦎✂
✂💎
📄✂
💎🦎
🖖💎
💎🖖
📄🦎
🖖📄
✂🖖
✂🦎
💎📄
🖖🖖
✂✂
🦎🦎
📄📄
🖖✂
💎✂
✂📄
📄🖖
🦎📄'''.split("\n")

import re
w="'✂ cuts 📄 covers 💎 crushes 🦎 poisons 🖖 smashes ✂ decapitates 🦎 eats 📄 disproves 🖖 vaporizes 💎 crushes ✂'"
for a,b in sys.argv[1:]:  
    print("Tie" if a==b else re.findall(f"({a}|{b})\s\w+\s({a}|{b})",w)[0])

    
    
