import numpy as py
import mcit as mc

def f(x):
  return 0.5*x**3

integral = mc.MCintegrate(f,0,1,9999)

print(f"integral = {integral: 0.3f}")