def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def main():
    print("Temperature Conversion Program")
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of the temperature (C, F, K): ").strip().upper()

    if unit == 'C':
        print(f"{temp}°C is equal to {celsius_to_fahrenheit(temp):.2f}°F")
        print(f"{temp}°C is equal to {celsius_to_kelvin(temp):.2f}K")
    elif unit == 'F':
        print(f"{temp}°F is equal to {fahrenheit_to_celsius(temp):.2f}°C")
        print(f"{temp}°F is equal to {fahrenheit_to_kelvin(temp):.2f}K")
    elif unit == 'K':
        print(f"{temp}K is equal to {kelvin_to_celsius(temp):.2f}°C")
        print(f"{temp}K is equal to {kelvin_to_fahrenheit(temp):.2f}°F")
    else:
        print("Invalid unit entered. Please enter C, F, or K.")

if __name__ == "__main__":
    main()

