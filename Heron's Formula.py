import math 
print("Area Of Triangle Calculator")
print("General Instructions: \n1. Enter the values accurately\n2. SI unit of area is square metre(m²)")
choice = int(input("You have \nA. If you have height, base and side then press 0\nB. If you have the length of all sides then press 1\nC. If you want to find height or base of a triangle then press 2\nMake a Choice: "))
if choice == 0:
    h = int(input("Enter the length of the height: "))
    b = int(input("Enter the length of the base: "))
    # Given height and base of the triangle
    unit = str(input("Unit of length entered(m/cm/km): "))
    area1 = 1/2 * b * h #Formula of the triangle 1/2 * base * height
    if unit in ("m", "cm", "km"): # If the unit is cm or m or km it will print the area
        print(f"Area of the triangle is {area1} {unit}²") # Printing the area
    else:
        print("Wrong input reload the whole session again") # If user inputs something else then it will print this
elif choice == 1: 
    a = int(input("Enter the length of the first side of the Triangle: ")) # Length of first side
    b = int(input("Enter the length of the second side of the Triangle: ")) #Length of second side
    c = int(input("Enter the length of the third side of the Triangle: "))# Length of third side
    unit_2 = str(input("Unit of length entered(m/cm/km): "))
    # Using the Herons Formula
    s = (a+b+c)/2 # Finding the semi-perimeter
    d = (s-a) * (s-b) * (s-c)
    area = math.sqrt(s * d)
    if unit_2 in ("m", "cm", "km"): # Same logic used in previous section
        print(f"Area of the triangle: {area} {unit_2}²")  # Prints the output
    else:
        print("Wrong input reload the whole session again")
elif choice == 2:
    choose = int(input("To find: \npress 1 for height\npress 2 for base")) # Asks user what he wants to find
    if choose == 1: # If User chooses to find height
        base = int(input("Enter the length of base: ")) # Asks the length of the base
        area2 = int(input("Enter the area of the triangle: ")) # Asks the Area of the triangle
        unit_3 = str(input("Unit of length entered(m/cm/km): "))
        height = 2*area2/base # Formula to find the height
        if unit_3 in ("m", "cm", "km"): # Same logice as used in previous section
            print(f"Height of the triangle  is {height} {unit_3}") # Height of the triangle is printed
        else:
            print("Wrong input reload the whole session again")
    if choose == 2: # If User chooses to find base
        height = int(input("Enter the length of height: ")) # Asks the length of the height
        area3 = int(input("Enter the area of the triangle: ")) # Asks the area
        unit_4 = str(input("Unit of length entered(m/cm/km): ")) 
        base = 2*area3/height # Formula to find the base
        if unit_4 in ("m", "cm", "km"): #Sane logic as used in previous section
            print(f"Height of the triangle  is {base} {unit_4}") # Base of the triangle is printed
        else:
            print("Wrong input reload the whole session again")
else:
    print("Wrong input, reload the session again")
