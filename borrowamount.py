#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:34:27 2023

@author: daivd piolo
"""
def calculate_affordable_loan_amount(payment, r, n):
    monthly_interest_rate = r / (12 * 100)  # Convert APR to monthly interest rate
    numerator = payment
    denominator = monthly_interest_rate * ((1 + monthly_interest_rate) ** n)
    loan_amount = numerator / denominator
    return loan_amount


def calculate_monthly_repayment(PV, r, n):
    monthly_interest_rate = r / (12 * 100)  # Convert APR to monthly interest rate
    numerator = monthly_interest_rate * PV
    denominator = 1 - (1 + monthly_interest_rate) ** -n
    monthly_repayment = numerator / denominator
    return monthly_repayment

cont = True

while (cont == True):
  choice = int(input('enter choice. 1 for PV, 2 for Pmt, 0 to exit \n'))
  if (choice == 1): 
    cont = False
    
    # Get user inputs for PV, r, and n
    PV = float(input("Enter the Present Value (PV): "))
    r = float(input("Enter the Annual Percentage Rate (r): "))
    n = int(input("Enter the number of months (n): "))
    
    monthly_repayment_amount = calculate_monthly_repayment(PV, r, n)
    print("Monthly repayment amount: $", round(monthly_repayment_amount, 2))
  
  elif (choice == 2):
    cont = False
  
    # Get user inputs for payment, r, and n
    payment = float(input("Enter the desired monthly payment amount: "))
    r = float(input("Enter the Annual Percentage Rate (r): "))
    n = int(input("Enter the number of months (n): "))
    
    affordable_loan_amount = calculate_affordable_loan_amount(payment, r, n)
    print("Maximum affordable loan amount: $", round(affordable_loan_amount, 2))
  else:
    print('please choose 1 or 2')
  

