def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in meters.
    """
    bmi = weight / (height ** 2)
    return bmi

def main():
    print("Welcome to the BMI Calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)

    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("Your weight is normal.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

if __name__ == "__main__":
    main()
