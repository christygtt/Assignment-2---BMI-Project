# test_bmi.py

from bmi import height_to_inches, calculate_bmi, bmi_category


# --- height tests ---
def test_height_conversion():
    assert height_to_inches(5, 10) == 70


# --- bmi calculation ---
def test_bmi_calculation():
    assert calculate_bmi(150, 65) == 25.0


# --- boundary tests ---
def test_underweight():
    assert bmi_category(18.4) == "Underweight"


def test_normal_lower():
    assert bmi_category(18.5) == "Normal weight"


def test_normal_upper():
    assert bmi_category(24.9) == "Normal weight"


def test_overweight_lower():
    assert bmi_category(25.0) == "Overweight"


def test_overweight_upper():
    assert bmi_category(29.9) == "Overweight"


def test_obese():
    assert bmi_category(30.0) == "Obese"