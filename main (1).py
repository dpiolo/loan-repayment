#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
"""
Created on Wed Jun 14 18:34:27 2023

@author: daivd piolo
"""
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

cont = True

while (cont == True):
  choice = int(input('Enter Choice: 1 for PMT, 2 for Present Value, 3 for Num months, 0 to exit \n'))
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
  elif (choice == 3):
        payment = float(input("Enter the desired monthly payment amount: "))
        PV = float(input("Enter the Present Value (PV): "))
        r = float(input("Enter the Annual Percentage Rate (r): "))
        
        num_months = calculate_months(payment,PV,r)
        print("Num months to pay:", round(num_months,2))
  else: 
    exit()