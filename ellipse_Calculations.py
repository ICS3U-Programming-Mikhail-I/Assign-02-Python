import math

def calculate_area(a, b):
    """Calculate the area of the ellipse."""
    return math.pi * a * b

def calculate_perimeter(a, b):
    """Calculate the perimeter of the ellipse using Ramanujan's approximation."""
    h = ((a - b)**2) / ((a + b)**2)
    perimeter = math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
    return perimeter

def get_positive_float(prompt):
    """Get a positive float from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a value greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a positive number.")

def run_test_cases():
    """Function to run test cases for area and perimeter."""
    test_cases = [
        {"a": 5, "b": 3},
        {"a": 10, "b": 6},
        {"a": 7, "b": 7},
        {"a": 3, "b": 2},
        {"a": 15, "b": 10},
        {"a": 20, "b": 5},
    ]
    
    for i, case in enumerate(test_cases, start=1):
        a, b = case["a"], case["b"]
        area = calculate_area(a, b)
        perimeter = calculate_perimeter(a, b)
        
        print(f"Test Case {i}: a={a}, b={b}")
        print(f"Area: {area:.2f} square units")
        print(f"Perimeter (approx): {perimeter:.2f} units\n")

def main():
    print("Welcome to the Ellipse Calculator!\n")
    
    # Run test cases
    run_test_cases()

    # Option to calculate user-input ellipse
    while True:
        # Get user input for major and minor axes
        a = get_positive_float("Enter the length of the major axis (a): ")
        b = get_positive_float("Enter the length of the minor axis (b): ")

        # Calculate area and perimeter
        area = calculate_area(a, b)
        perimeter = calculate_perimeter(a, b)

        # Output results
        print(f"\nEllipse with axes a={a} and b={b}:")
        print(f"Area: {area:.2f} square units")
        print(f"Perimeter (approx): {perimeter:.2f} units\n")

        # Option to calculate another ellipse
        another = input("Do you want to calculate for another ellipse? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
