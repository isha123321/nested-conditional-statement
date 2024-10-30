medical_cause=input("do you have a medical cause Y or N :")
attendance=int(input("what is the attendance of the student:"))
if medical_cause  == "Y":
    print("you are allowed")
else :
    if attendance>=75:
        print("you are allowed")
    else:
        print("you are not allowed")    