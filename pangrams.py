import sys
for a in sys.argv[1:]:
	if all(chr(x)in a.lower()for x in range(97,123)):
		print(a)
