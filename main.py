# main.py

from bmi import height_to_inches, calculate_bmi, bmi_category


def main():
    feet = int(input("Enter height (feet): "))
    inches = int(input("Enter height (inches): "))
    weight = float(input("Enter weight (lbs): "))

    height = height_to_inches(feet, inches)
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    print(f"\nBMI: {bmi}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()