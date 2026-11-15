#Class creation
class myClass:

      #private variable
    __privatevar = 27;

    #private method
    def __privmeth(self):
        print("i'm inside class myclass")

    #function to print value of private variable
    def hello(self):
        print("Private Variable value:", myClass.__privatevar)
        
#Object creation and method call
foo = myClass()
foo.hello()
foo.__privmeth()