#ATM Password Retry system



"""concepts used 
input/output
conditionals 
while loop"""



print("==== ATM Password Retry System ====")

# Correct password
correct_password = "Admin123"

# Total attempts
count = 3

while count > 0:

    password = input("Enter your Password: ")

    if password == correct_password:
        print("Access Granted")
        break

    else:
        count -= 1 #decreas attempts with 1

        print("Wrong Password!")
        print("Attempts Left:", count) # here counts attempts

if count == 0:
    print("Card Blocked")