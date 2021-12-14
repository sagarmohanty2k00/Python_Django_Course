# Input is a day of the week

inp = input("Enter toda's day : ").upper()
vegDays = ["MONDAY", "TUESDAY", "THURSDAY", "SATURDAY"]

if inp in vegDays:
    print("You can not have chicken tonight.")
else :
    print("You can have chicken tonight.")