#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 17:10:50 2023

@author: djhoannapiolo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
"""
Created on Wed Jun 14 18:34:27 2023

@author: daivd piolo
"""

#############################################################################################
def calculate_affordable_loan_amount(payment, r, n):
    monthly_interest_rate = r / (12 * 100)  # Convert APR to monthly interest rate
    numerator = 1 - (1 + monthly_interest_rate) ** (-n)
    denominator = payment / monthly_interest_rate
    loan_amount = numerator * denominator
    return loan_amount


def calculate_monthly_repayment(PV, r, n):
    monthly_interest_rate = r / (12 * 100)  # Convert APR to monthly interest rate
    numerator = monthly_interest_rate * PV
    denominator = 1 - (1 + monthly_interest_rate) ** -n
    monthly_repayment = numerator / denominator
    return monthly_repayment
  
# n = log(1-PV*r/pmt) / log(1+r)
def calculate_months(pmt, PV, r):
    monthly_interest_rate = r / (12 * 100)  # Convert APR to monthly interest rate
    
    num_months = -np.log(1-PV*monthly_interest_rate/(pmt))/np.log(1+monthly_interest_rate)
    return num_months

def computesR(pmt, PV, n):
    rLow = 0
    rHigh = 0.5
    diff = 2
    while abs(diff) > 0.001:
        rTry = (rLow + rHigh)/2
        diff = pmt - PV*rTry/(1-(1+rTry)**(-n))
        if diff > 0:
            # pmt too high, increase r
            rLow = rTry
        else:
            rHigh = rTry
    return rTry
def printSection():
    print("-------------------------------------------------------")
    
def askCont():
    answer = input("Would you like to calculate something else?\nType 'y' for Yes\nType 'n' for No\n")
    print(answer)
    if answer == 'y':
        return True
    else:
        return False
#############################################################################################

cont = True
print("============")
print("| Welcome! |")
print("============")


while (cont == True):
  choice = int(input('Enter Choice:\n1: Calculate Payment\n2: Calculate Present Value\n3: Calculate Number of Months\n4: Calculate APR\n0: Quit Program  \n'))
  
  
  if (choice == 1): 
    
    printSection()
    # Get user inputs for PV, r, and n
    PV = float(input("Enter the Present Value (PV): $"))
    r = float(input("Enter the Annual Percentage Rate (r): "))
    n = int(input("Enter the number of months (n): "))
    
    monthly_repayment_amount = calculate_monthly_repayment(PV, r, n)
    printSection()
    print("Monthly repayment amount: $",round(monthly_repayment_amount, 2))
    printSection()
    cont = askCont()
    printSection()
    
    
  elif (choice == 2):

    printSection()
  
    # Get user inputs for payment, r, and n
    payment = float(input("Enter the desired monthly payment amount: $"))
    r = float(input("Enter the Annual Percentage Rate (r): "))
    n = int(input("Enter the number of months (n): "))
    
    affordable_loan_amount = calculate_affordable_loan_amount(payment, r, n)
    printSection()
    print("Maximum affordable loan amount: $", round(affordable_loan_amount, 2))
    printSection()
    cont = askCont()
    printSection()
  elif (choice == 3):
     cont = False
     printSection()
     payment = float(input("Enter the desired monthly payment amount: $"))
     PV = float(input("Enter the Present Value (PV): $"))
     r = float(input("Enter the Annual Percentage Rate (r): "))
        
     num_months = calculate_months(payment,PV,r)
     printSection()
     print("Num months to pay:", round(num_months,2))
     printSection()
     cont = askCont()
     printSection()
  elif (choice == 4):
        cont = False
        printSection()
        payment = float(input("Enter the desired monthly payment amount: $"))
        PV = float(input("Enter amount borrowed (PV): $"))
        n = int(input("Enter the number of months (n): "))
        
        if payment * n > PV:
            rate = computesR(payment,PV,n)
            rate = rate * 1200  
            printSection()
            print(f"Interest Rate: {rate: 0.2f}% APR")
            printSection()
            cont = askCont()
            printSection()
            
        else: 
            printSection()
            print("No solution, pmt * n must be > PV\n")
            printSection()
  else: 
    printSection()
    print("Goodbye!")
    printSection()
    exit()
    

print("Goodbye!")
printSection()
