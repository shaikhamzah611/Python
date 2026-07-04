
test_dict = {
    "Codingal": 3,
    "is": 2,
    "best": 2,
    "for": 2,
    "Coding": 1
}

print("Dictionary:", test_dict)

value = int(input("Enter the value to check its frequency: "))

frequency = list(test_dict.values()).count(value)

print("Frequency of", value, "is", frequency)