def gallons_to_liters(galloM):
    return galloM * 3.785

while True:
    gallon = float(input("Enter a volume in American gallons (negative value to quit): "))
    if gallon < 0:
        print("Program finished.")
        break
    liters = gallons_to_liters(gallon)
    print(f"{gallon:.1f} American gallons is {liters:.2f} liters.")