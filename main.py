def body_surface_area(weight, height):
    print("Calculates Body surface area (BSA) from your height and weight:")
    height = eval(height)
    weight = eval(weight)
    bsa = 0.007184 * (weight**0.425)  * (height**0.725)
    print(f"Your Body Surface Area: {bsa} cm2")
    return bsa