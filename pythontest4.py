class book:
    def __init__(self,borrow,retun):
        self.borrow = borrow
        self.retun = retun
    def borrowed(self):
        if self.borrow==True:
            print("Confirmation:Yes")
        else:
            print("Confirmation:No")
    def retunbook(self):
        if self.retun==True:
            print("Ok")
        else:
            print("No")
math = book("Math")
science = book("Science")
social = book("Social")

math.borrowed()
science.borrowed()
social.borrowed()