file=open("fileNew.txt",'r')
r=file.readlines()
fileWrite=open("FileNewWrite.txt",'w')
for i in range(0,len(r)):
    if i%2!=0:
        p=fileWrite.write(r[i])
file.close()
New=open("FileNewWrite.txt",'r')
count=New.read()
print(count)
New.close()
