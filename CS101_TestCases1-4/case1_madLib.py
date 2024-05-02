# Need to cover the following topics:
#   print function                                      
#   input function                                     
#   changing values  str, int, float()                 
#   comments                                           
#   artithmetic op                                     
#   variables and how to use them                       
#   modules                                          

# Made by Michael H on 1/6/23
name          = "John Doe"
age           = 20
company       = "Mayo Clinic"
currentAnnualIncome = 15250
graduationTime     = 2.5
projectedAnnualIncome    = 35700
incomePerHour            = (projectedAnnualIncome / 52) / 38

print("Hello, my name is " + name + "! \nI am " + str(age) + " years old, and go to university.")
print("I want to work at " + company + " when I finish college. As of right now I do part-time work", end=" ")

# updating variables
company = "Oakland University"

print(" at " + company + " at the front desk. When I am " + str(graduationTime + age) + ".")
print("That will be in " + str(graduationTime) + " years from now, when I hope to make $", end="")
print(str(round(incomePerHour - (currentAnnualIncome / 52) / 38, 2)) + " more per hour than I did previously.")