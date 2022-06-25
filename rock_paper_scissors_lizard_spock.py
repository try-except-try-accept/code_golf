import sys, re
w="'✂ cuts 📄 covers 💎 crushes 🦎 poisons 🖖 smashes ✂ decapitates 🦎 eats 📄 disproves 🖖 vaporizes 💎 crushes ✂'"
for a,b in sys.argv[1:]:  
    print("Tie" if a==b else re.search(f"({a}|{b})\s\w+\s({a}|{b})",w).group())
