str=str(input("Enter A String:\n"))
count=0
n=len(str)
for i in range(0,n):
    if (str[i]!=" "):
        count=count+1
        i=i+1
print("Total Characters in",str,"is:\n",count)

    