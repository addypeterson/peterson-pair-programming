def feetinch2meters (feet, inches):         # This function looks correct and is easy to read! 
    total_inches = (12*feet)+inches         # You convert all feet to inches then convert the total inches to meters 
    total_meters = total_inches/39.3701     
    return total_meters                     

f = float(input("Input feet: "))            # This is where the user inputs their feet and inches
i = float(input("Input inches: "))

result = feetinch2meters(f, i)

print(f"Result: {result} meters")           # Where you output the result in meters! Good job!