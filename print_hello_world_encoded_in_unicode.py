s,a="񰝆򖺔𨊖򆖌񬜒瞏񲛦񂝉","".join
i=a([hex(ord(u)-32)[2:].zfill(5)for u in s])
exec(a([chr(int(i[j:j+2],16))for j in range(0,len(i),2)]))
