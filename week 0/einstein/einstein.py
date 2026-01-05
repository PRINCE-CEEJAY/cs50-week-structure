def calculateEinsteinJoules(mass):
    joules = int(mass) * pow(300000000, 2)
    return joules

result = input("Enter the mass to be calculated ")

print(calculateEinsteinJoules(result))

