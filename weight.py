from convertors import *
weight = int(input("Weight: "))
unit = input("(L)bs OR (k)g: ")

if unit.upper() == "L":
   print(f"You are of {lbs_to_kg(weight)} KiloGrams")
else:
   print(f"You are of {kg_to_lbs(weight)} Pounds")
