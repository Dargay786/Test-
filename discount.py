age = int(input("Enter your age:"))
std = input("Are you a student?yes/no:")

if (age <= 12):
    print ("you are elligible for discount")
elif (13 >= age <= 18 and std == "yes"):
    print("you are elligible for discount")
else:
    print("you are not elligible for discount")

    

