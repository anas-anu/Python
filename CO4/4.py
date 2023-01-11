class Time:
    def __init__(self):
        self.__h=int(input("Enter Hour:\n"))
        self.__m=int(input("Enter Minute:\n"))
        self.__s=int(input("Enter Secound:\n"))
    def __add__(self,other):
        hrs=self.__h + other.__h
        print("Sum of Hours:\n",hrs)
        mnt=self.__m + other.__m
        print("Sum of Minutes:\n",mnt)
        sec=self.__s + other.__s
        print("Sum of Secounds:\n",sec)
        if mnt>=60:
            hrs=hrs+1
            mnt=mnt-60
        if sec>=60:
            mnt=mnt+1
            sec=sec-60
        return hrs,mnt,sec
print("First Time:")
a=Time()
print("Second Time:")
b=Time()
add=a+b
print("Add",add)