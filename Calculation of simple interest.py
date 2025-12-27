principal=float(input("Enter the principal amount : "))
rate=float(input("Enter the interest rate (%) : "))
time=float(input("Enter the time period (in years) : "))
simple_interest=(principal*rate*time)/100
total_amount=principal+simple_interest
print("Principal amount : ",principal)
print("Interest rate : ",rate,"%")
print("Time period : ",time,"years")
print("Simple interest : ",simple_interest)
print("Total amount : ",total_amount)
