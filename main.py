#map & cheese
#welcome message
print("\n -------------------------------------------------------------------------")
print("Welcome to Map & Cheese! Est. 2021 to find hungry people good food!")
print("Visit our website -> www.mapandcheese.com")
print("Follow us on Instagram @mapandcheese")
print("\n ------------------------------------------------------------------------")

#ask f/l name and age
fname = input("Please enter your first name: ")
lname = input("Please enter your last name: ")
age = int(input("Please enter your age: "))
print(f"Full Name: {fname} {lname}")
cname = input("Is the name you entered above correct? ")
if cname != "yes":
    fname = input("Please enter your first name: ")
    lname = input("Please enter your last name: ")
    print(f"Updated Full Name: {fname} {lname}")
c_age = input("Is the age you entered correct?")
if c_age != "yes":
    age = int(input("Please enter your age: "))
    print(f'Updated age: {age}')
# ask for phone number
pnum = input("Please enter your phone number: ")
print(f"Phone Number: {pnum}")
cpnum = input("Is the phone number you entered above correct?")
if cpnum != "yes":
    pnum = input("Please enter your phone number: "))
    print(f"Updated Phone Number: {pnum}")
# ask if they want takeout or delivery
opt = input("Would you like to look for takeout or delivery options? ")
# ask for 

