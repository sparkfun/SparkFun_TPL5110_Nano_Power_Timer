import math
import itertools

#5 Set values of resistors 
#Add a 6th value to resistor array if you add a custom resistor. You can then
#uncomment the code that is precluded by "Uncomment for sixth resistor" to
#calculate all combinations of values.
resistorArr = [16200, 22000, 92000, 125000, 170000]
letterEquiv = ["A", "B", "C", "D", "E"]

#Parallel resistance formula
def calculate_resistance(*args):
    totalResistance = 0 
    for arg in args:
        totalResistance += 1/arg 
    finalRes = (1/totalResistance)
    return finalRes

def equationOne(resistance):

def equationOne(resistance):
def equationOne(resistance):

#Let's see the list of all combination of resistors. 
print("---------Lists of all combinations of Resistors-----------\n")
print("Combinations of 2:")
comboTwo = list(itertools.combinations(resistorArr, 2))
print(list(itertools.combinations(letterEquiv, 2)))
#print(comboTwo)
print("")

print("Combinations of 3:")
comboThree = list(itertools.combinations(resistorArr, 3))
print(list(itertools.combinations(letterEquiv, 3)))
#print(comboThree)
print("")

print("Combinations of 4:")
comboFour = list(itertools.combinations(resistorArr, 4))
print(list(itertools.combinations(letterEquiv, 4)))
#print(comboFour)
print("")

print("Combinations of 5:")
comboFive = list(itertools.combinations(resistorArr, 5))
print(list(itertools.combinations(letterEquiv, 5)))
#print(comboFive)
print("")

#Uncomment for sixth resistor value
#print("Combinations of 6:")
#comboSix = list(itertools.combinations(resistorArr, 6))
#print(comboSix)
#print("")

print("------Calculated Resistance------\n")
print("Resistance for pairs of Resistors:")
total = 0
for res1, res2 in comboTwo:
    print(calculate_resistance(res1, res2))
    total += 1 
print(total)
print("")

total = 0
print("Resistance for trios of Resistors:")
for res1, res2, res3 in comboThree:
    print(calculate_resistance(res1, res2, res3))
    total += 1 
print(total)
print("")

total = 0
print("Resistance for quads of resistors:")
for res1, res2, res3, res4 in comboFour:
    print(calculate_resistance(res1, res2, res3, res4))
    total += 1 
print(total)
print("")

total = 0
print("Resistance when five are combined:")
for res1, res2, res3, res4, res5 in comboFive:
    print(calculate_resistance(res1, res2, res3, res4, res5))
    total += 1 
print(total)
print("")

#Uncomment when sixth value is determined
#print("Resistance when all are combined:")
#for res1, res2, res3, res4, res5, res6 in comboFive:
#    print(calculate_resistance(res1, res2, res3, res4, res5, res6))
#print("")
