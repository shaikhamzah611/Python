class myclass:

    __privvar = 27;
    def __privmeth(self):
        print("I am in my class")
    def hello(self):
        print("Private variable value: ",myclass.__privvar)
foo = myclass()
foo.hello()
foo.__privmeth