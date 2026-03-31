def feetinch2meters (feet, inches):         #function definition
    total_inches = (12*feet)+inches         #all to inches  
    total_meters = total_inches/39.3701     #convert
    return total_meters                     #spit out new number

f = float(input("Input feet: "))
i = float(input("Input inches: "))

result = feetinch2meters(f, i)

print(f"Result: {result} meters")