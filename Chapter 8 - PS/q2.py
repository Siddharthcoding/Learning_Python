def convertedTemp(celcius):
    return (celcius * 9/5) + 32

celcius = float(input("Enter temperature in Celcius: "))
print(f"The temperature in Fahrenheit is: {round(convertedTemp(celcius), 2)}")