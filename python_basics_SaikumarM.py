name ="Sai"
age=30
height=5.7
is_student=False
#print all for values in single print statement
print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")

#Task 2: String Formatting
print (f"Name: {name} | Age: {age} | Height: {height} | Is Student: {is_student}")

#Tas 3: Arithmetic Operations
print("\n------Arithmetic Results------------")
#Age in Months
age_in_months=age*12
print(f"Age in months: {age_in_months}")
#Age in Days
age_in_days=age*365
print(f"Age in days: {age_in_days}")
#The remainder when age is divided by 7
reminder=age%7
print(f"Reminder when divided by 7: {reminder}")
#Age raised to the power of 2
age_squared=age ** 2
print(f"Age raised to the power of 2: {age_squared}")
