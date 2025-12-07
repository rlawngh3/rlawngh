s=input()
r=""
i=0
while i<len(s):
    if i+1<len(s) and s[i:i+2]=="XX":
        r+="AAAA" if (i+2<len(s) and s[i+2]=="X") else "BB"
        i+=2
    else:
        r+=s[i]
        i+=1
print(-1 if "X" in r else r)
