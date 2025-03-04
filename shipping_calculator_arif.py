# Express Shipping Rate Calculator
# Developer: Kevin O'Brien
# Last Updated: March 2024

# Show program header
print("Welcome to Package Express. Please follow the instructions below.")

# Get package weight
weight_value = float(input("Please enter the package weight:\n"))

# Weight limit validation
if weight_value > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()

# Get package dimensions
dimension_w = float(input("Please enter the package width:\n"))
dimension_h = float(input("Please enter the package height:\n"))
dimension_l = float(input("Please enter the package length:\n"))

# Calculate total dimensions
total_dimensions = dimension_w + dimension_h + dimension_l

# Size limit validation
if total_dimensions > 50:
    print("Package too big to be shipped via Package Express.")
    exit()

# Calculate shipping cost
# Cost = (width * height * length * weight) / 100
shipping_cost = (dimension_w * dimension_h * dimension_l * weight_value) / 100

# Display shipping cost
print(f"Your estimated total for shipping this package is: ${shipping_cost:.2f}")
print("Thank you!") 