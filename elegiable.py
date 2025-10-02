attendence=int(input("enter the attendence"))
medical_couse=input("had medical couse yes/no")

if attendence>75:
    print("allowed to write exam")
else:
    if medical_couse="yes":
        print("permitted to write exam")
       else:
        print("not allowed")     