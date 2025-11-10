import sys
if  len(sys.argv) ==2:
  script_salary = sys.argv[0]
  salary = sys.argv[1]
  print("User provided inputs values:")
else:
   script_salary = sys.argv[0]
   salary = "6000"

bonus = 0.10*salary
total_salary = bonus+ salary
print("Bonus Amount: ₹", bonus)
print("Total Salary: ₹", total_salary)
