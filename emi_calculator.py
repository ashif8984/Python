#!/usr/bin/python3


'''
EMI Calculator
- Enter the Type of Loan, Loan Amount, Loan Period
- Get the Monthly EMI for the same.

Future Updates-
- More Functionality: Mortage Calculator
- Simple User Input
- Better Display
- OOP Implentation

Instruction:
-Install prettytable module if not present as-
pip install PrettyTable

'''

# import PrettyTable for Tabular Data representation
from prettytable import PrettyTable


# Function to Calculate Compound Interest
def emi_func(p , n, r):

    i = float(r/(12*100))
    x = float((1+i) ** n)
    y = float(x / (x - 1))
    emi = float((p * i) * y)
    return emi

# Function to fetch type of Loan 
def loan_type(instrument,rate):
    print("Enter the Amount for the %s Loan=" %instrument)
    principal = int(input())
    time = int(input("Enter Loan Term:"))
    answer = emi_func(principal, time, rate)
    print("Your EMI for "+instrument+" is = " + str(round(answer, 2)) + "/month ")


print("Welcome to EMI Calculator!!")
print("The Rates for the Loans are:")

x = PrettyTable()

x.field_names = ["Asset","Rate of Interest(ROI)"]
x.add_row(["1.Car Loan: ","12%" ])
x.add_row(["2.Home Loan: ","17.5%" ])
x.add_row(["3.Personal Loan: ","10.5%" ])

print(x)


print("Choose any option from the above (press 1, 2 or 3):")
user_input = int(input())


if user_input == 1:
    loan_type('Car Loan', 12)
elif user_input == 2:
    loan_type('Home Loan',17.5)
else:
    loan_type('Personal Loan',10.5)



