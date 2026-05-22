medical_cause = (input("Did you have a medical cause(Yes/No):")).strip().upper()

if medical_cause=="Yes":
    print("You are allowed")

else:
    
    atten = int(input("Enter the attendance of the student:"))

if atten >= 75:
    print("Allowed")

else:
    print("Not Allowed")