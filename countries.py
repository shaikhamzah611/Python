class India():
    def cap(self):
        print("New Delhi is capital of India")
    def lang(self):
        print("Hindi is most widely spoken language in India")
    def type(self):
        print("India is a developing country")
class USA():
    def cap(self):
        print("Washington,D.C is capital of USA")
    def lang(self):
        print("English is the primary language in USA")
    def type(self):
        print("USA is a developed country")

class Japan():
    def cap(self):
        print("Tokyo is capital of Japan")
    def lang(self):
        print("Japanese is the primary language in Japan")
    def type(self):
        print("Japan is a developed country")

ind = India()
usa = USA()
japan = Japan()

for country in (ind,usa,japan):
    country.cap()
    country.lang()
    country.type()