#Angelina Del Vicario
#09/30/26
#CMP131
#Lab 06

package = input("Select a package (A, B, or C)")

minutes = int(input("Enter number of minutes used: "))

if package == "A":
    bill = 39.99
    if minutes > 450:
        bill = bill + (minutes - 450) * 0.45
elif package == "B":
    bill = 59.99
    if minutes > 900:
        bill = bill + (minutes - 900) * 0.40
elif package == "C":
    bill = 69.99
else: print ("Invalid Package selected")


print(" Total Monthly Bill: $ ",bill)
