

import math
print("investment - to calculate the amount of interest you will earn on your investment")
print("bond - to calculate the amount of investment you will have to pay on a home loan")

user_option = input("Enter either 'investment' or 'bond' from the above to proceed:\n").lower()
# initial inpput for investment choice
if user_option == "investment": 
   deposited_amount = float(input("how mauch amount you want to deposit?\n"))
   interest_rate = float(input("what is the interest rate they exepct for?\n"))
   interest_rate_float = float(interest_rate/100)
   investment_period = float(input("for how many years you want to invest?\n"))
   type_of_interest_rate = input("Enter your choice of interest rate either 'simple' or 'compound':\n")
    # input for interest rate choice
   if type_of_interest_rate == 'simple': 
       money_return = deposited_amount * (1 + interest_rate_float*investment_period)
       print(f"the return you will get from your investment will be £{money_return:.2f}")

   elif type_of_interest_rate == 'compound':
       money_return_compound = deposited_amount * math.pow((1 + interest_rate_float), investment_period)
       money_return_compound_2deci = float("{:.2f}".format(money_return_compound))
       print(f"the return you will get from your investment will be £{money_return_compound_2deci:.2f}")
      
   else:
       print("Wrong choice enter")
 # input for bond choice
elif user_option == "bond".lower():
     house_value = float(input("What is the present value of the house?\n"))
     interest_rate = float(input("What is the interest rate you expects for?\n"))
     bond_interest_monthly = float(interest_rate/12/100)
     number_of_months= float(input("How many months do you plan to take for repaying the bond?\n"))
     repayment = (bond_interest_monthly * house_value)/(1 - (1 + bond_interest_monthly)**(-number_of_months))
     repayment_2deci = float("{:.2f}".format(repayment))
     print(f"the return will be received from you bond will be £{repayment_2deci:.2f}")

else:
     print("Wrong choice entered")


   