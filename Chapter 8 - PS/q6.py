def convertedLength(inch):
    return inch * 2.54

inch = float(input("Enter length in inches: "))
print(f"The length in centimeters is: {convertedLength(inch)}")