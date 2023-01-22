class Publisher():
    def __init__(self,t,a):
        self.__title=t
        self.__author=a
    def display(self):
        print("Title is:",self.__title)
        print("Author:",self.__author)
class Book(Publisher):
    def __init__(self,t,a,p,n):
        super().__init__(self,t,a)
        self.__price=p
        self.__no_of_pages=n
    def display(self):
        print("Price:",self.__price)
        print("Number of Pages:",self.__no_of_pages)
class Python():
    def __init__(self,t,a,p,n):
        self.__title=t
        self.__author=a
        self.__price=p
        self.__no_of_pages=n
    def display(self):
        print("Title:",self.__title)
        print("Author:",self.__author)
        print("Price:",self.__price)
        print("Number of Pages:",self.__no_of_pages)
obj=Python("Book1","Anas","1000","100")
obj.display()

