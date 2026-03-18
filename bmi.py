def height_to_inches(feet, inches):
    return feet * 12 + inches

def calculate_bmi(weight, height_inches):
    return round((703 * weight) / (height_inches ** 2), 1)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"