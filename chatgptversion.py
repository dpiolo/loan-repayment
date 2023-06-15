#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:34:27 2023

@author: daivd piolo
"""

def calculate_monthly_repayment(PV, r, n):
    monthly_interest_rate = r / (12 * 100)  # Convert APR to monthly interest rate
    numerator = monthly_interest_rate * PV
    denominator = 1 - (1 + monthly_interest_rate) ** -n
    monthly_repayment = numerator / denominator
    return monthly_repayment

# Get user inputs for PV, r, and n
PV = float(input("Enter the Present Value (PV): "))
r = float(input("Enter the Annual Percentage Rate (r): "))
n = int(input("Enter the number of months (n): "))

monthly_repayment_amount = calculate_monthly_repayment(PV, r, n)
print("Monthly repayment amount: $", round(monthly_repayment_amount, 2))
