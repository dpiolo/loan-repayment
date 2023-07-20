#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 17:40:48 2023

@author: djhoannapiolo
"""

import completed as ls


PV = 1000
r = 5
n = 12
pmt = ls.calculate_monthly_repayment(PV,r,n)
print(f"pmt = ${pmt}")

pmt2 = ls.calculate_monthly_repayment(1000,5,12)
print(f"and the pmt also is ${pmt2}")