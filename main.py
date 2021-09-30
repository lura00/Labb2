def body_surface_area():
    print("Calculates Body surface area (BSA) from your height and weight:")
    height = input ("Enter your height (cm): ")
    weight = input ("Enter your weight (kg): ")
    height = eval(height)
    weight = eval(weight)
    bsa = 0.007184 * (weight**0.425)  * (height**0.725)
    print(f"Your Body Surface Area: {bsa} cm2")