def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)


def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)


def main():
    """Main function to handle user input and perform conversions."""
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    try:
        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
        elif choice == 2:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")
        elif choice == 3:
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius}°C is {celsius_to_kelvin(celsius)}K")
        elif choice == 4:
            kelvin = float(input("Enter temperature in Kelvin: "))
            print(f"{kelvin}K is {kelvin_to_celsius(kelvin)}°C")
        elif choice == 5:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit}°F is {fahrenheit_to_kelvin(fahrenheit)}K")
        elif choice == 6:
            kelvin = float(input("Enter temperature in Kelvin: "))
            print(f"{kelvin}K is {kelvin_to_fahrenheit(kelvin)}°F")
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


if __name__ == "__main__":
    main()
