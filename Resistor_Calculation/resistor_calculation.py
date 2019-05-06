import math

#38 values here...
resistorArr = [ 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5200, 
                6790, 7640, 8300, 8850, 9270, 9710, 10180, 10680, 11200, 14410, 
                16780, 18750, 20047, 22000, 29350, 34000, 39000, 43000, 52000, 55000, 
                57000, 77000, 92000, 104000, 115000, 124000, 149000, 170000]

def calculate_resistance(*args):
    for arg in args:
        totalResistance = 1/arg 
    
    finalRes = 1/totalResistance


#[[ calculate_resistance of n, n+1
#   calculate_resistance of n, n+1, n+2
#   calculate_resistance of n, n+1, n+2, n+3
#   calculate_resistance of n, n+1, n+2, n+3, n+4 ]]

#[[ calculate_resistance of n+1, n+2
#   calculate_resistance of n+2, n+3, n+4
#   calculate_resistance of n+1, n+2, n+3, n+4
#   calculate_resistance of n+1, n+2, n+3, n+4, n+5 ]]

def calculate_all():
    for resistor in resistorArr:
