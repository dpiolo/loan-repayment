#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 17:42:02 2023

@author: djhoannapiolo
"""

'''Use the formula Pmt = r * PV/(1-(1+r)**-n)

to write a python program to compute loan monthly repayment amount: Present Value (PV) = 12000, r = 7.45 (APR), n = 48 months

use a function that takes PV, r and n as inputs'''

pv = float(input("Present value: "))
r = float(input("R: "))
n = float(input("Num months: "))

def payment(present_value, rate, num_months):
   p = (rate * present_value)/(1-(1+r)**-num_months)
   return p

repayment = payment(pv,r,n)


print(f"Payment = ${repayment}")
