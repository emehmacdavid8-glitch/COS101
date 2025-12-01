print("Physics Formula Calculator")
print("Choose a formula:")
print("a → v = d / t")          # Speed
print("b → ρ = m / V")          # Density
print("c → P = F / A")          # Pressure
print("d → W = F × d")          # Work Done
print("e → P = W / t")          # Power

choice = input("Enter a, b, c, d, or e: ").lower()

# a → v = d / t
if choice == "a":
    print("\nFormula selected: v = d / t")
    d = float(input("Enter distance (d): "))
    t = float(input("Enter time (t): "))
    v = d / t
    print("Speed =", v, "m/s")

# b → ρ = m / V
elif choice == "b":
    print("\nFormula selected: ρ = m / V")
    m = float(input("Enter mass (m): "))
    V = float(input("Enter volume (V): "))
    rho = m / V
    print("Density =", rho, "kg/m³")

# c → P = F / A
elif choice == "c":
    print("\nFormula selected: P = F / A")
    F = float(input("Enter force (F): "))
    A = float(input("Enter area (A): "))
    P = F / A
    print("Pressure =", P, "N/m²")

# d → W = F × d
elif choice == "d":
    print("\nFormula selected: W = F × d")
    F = float(input("Enter force (F): "))
    d = float(input("Enter distance (d): "))
    W = F * d
    print("Work Done =", W, "Joules")

# e → P = W / t
elif choice == "e":
    print("\nFormula selected: P = W / t")
    W = float(input("Enter work done (W): "))
    t = float(input("Enter time (t): "))
    P = W / t
    print("Power =", P, "Watts")

else:
    print("Invalid option. Please run the program again.")