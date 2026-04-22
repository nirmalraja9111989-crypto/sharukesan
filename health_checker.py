# health_checker.py

def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than 0")
    return weight / (height ** 2)


def get_fitness_level(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=== Health Status Checker ===")

    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    bmi = calculate_bmi(weight, height)
    status = get_fitness_level(bmi)

    print(f"BMI: {bmi:.2f}")
    print(f"Fitness Level: {status}")


if __name__ == "__main__":
    main()