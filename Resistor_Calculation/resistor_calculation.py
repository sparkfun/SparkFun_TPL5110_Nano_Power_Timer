import math
import sys

#38 values here...
resistorArr = [16200, 22000, 92000, 125000, 170000]

def calculate_resistance(*args):
    totalResistance = 0 
    for arg in args:
        totalResistance += 1/arg 
    finalRes = (1/totalResistance)
    return finalRes

print("")
print("Calculate 1-5:")
print(calculate_resistance(resistorArr[0], resistorArr[1], resistorArr[2], resistorArr[3], resistorArr[4]))
print(calculate_resistance(resistorArr[0], resistorArr[1], resistorArr[2], resistorArr[3]))
print(calculate_resistance(resistorArr[0], resistorArr[1], resistorArr[2]))
print(calculate_resistance(resistorArr[0], resistorArr[1], resistorArr[3]))
print(calculate_resistance(resistorArr[0], resistorArr[1], resistorArr[4]))
print(calculate_resistance(resistorArr[0], resistorArr[2], resistorArr[3]))
print(calculate_resistance(resistorArr[0], resistorArr[2], resistorArr[3]))
print(calculate_resistance(resistorArr[0], resistorArr[3], resistorArr[4]))
print(calculate_resistance(resistorArr[0], resistorArr[1]))
print(calculate_resistance(resistorArr[0], resistorArr[2]))
print(calculate_resistance(resistorArr[0], resistorArr[3]))
print(calculate_resistance(resistorArr[0], resistorArr[4]))
print("")

print("Calculate 2-5:")
print(calculate_resistance(resistorArr[1], resistorArr[2], resistorArr[3], resistorArr[4]))
print(calculate_resistance(resistorArr[1], resistorArr[2], resistorArr[3]))
print(calculate_resistance(resistorArr[1], resistorArr[2]))
print(calculate_resistance(resistorArr[1], resistorArr[3]))
print(calculate_resistance(resistorArr[1], resistorArr[4]))
print("")

print("Calculate 3-5:")
print(calculate_resistance(resistorArr[2], resistorArr[3], resistorArr[4]))
print(calculate_resistance(resistorArr[2], resistorArr[3]))
print(calculate_resistance(resistorArr[2], resistorArr[4]))
print("")

print("Calculate 4-5:")
print(calculate_resistance(resistorArr[3], resistorArr[4]))
print("")
