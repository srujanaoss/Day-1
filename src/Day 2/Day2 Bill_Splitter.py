Amount = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people to split the bill: "))   
share= Amount / num_people
print("Total bill amount: ", Amount)
print(f"Each person should pay: {share:.2f}")
print(type("Amount"))
print(type(num_people))
print(type(share))


