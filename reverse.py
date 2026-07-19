class Reverse:
    def __init__(self, s=""):
        self.__s = s

    def reverse_string(self):
        return self.__s[::-1]


word = input("Enter a string: ")

obj = Reverse(word)

print("Reversed string:", obj.reverse_string())