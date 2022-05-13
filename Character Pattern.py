n=int(input())
i=1
while i<=n:
    j=1
    start=chr(ord('A')+i-1)
    while j<=i:
        charp=chr(ord(start)+j-1)
        print(charp,end="")
        j=j+1
    print()
    i=i+1
