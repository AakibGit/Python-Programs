import datetime

date = datetime.date.today()


print("----------------------------------------------------------------------------------------")
print("                                Age Calculator in Python ")
print("----------------------------------------------------------------------------------------")

print("Enter Your Birth of Date to know your Age")
userbirthyear = int(input("Enter your birth Year: "))
userbirthmonth = int(input("Enter your birth Month: "))
userbirthday = int(input("Enter your birth Day: "))

curr_age = date.year - userbirthyear

print("The current age is {}".format(curr_age))
