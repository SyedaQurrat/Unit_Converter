def convert_units(unit_type, unit_from, unit_to, value):

    if unit_type == "Length":
        if unit_from == "Meters" and unit_to == "Feet":
            return value * 3.28084  # Convert meters to feet
        # Add more length conversions as needed
    elif unit_type == "Weight":
        if unit_from == "Kilograms" and unit_to == "Pounds":
            return value * 2.20462  # Convert kilograms to pounds
        # Add more weight conversions as needed
    elif unit_type == "Temperature":
        if unit_from == "Celsius" and unit_to == "Fahrenheit":
            return (value * 9/5) + 32  # Convert Celsius to Fahrenheit
        # Add more temperature conversions as needed

    else:
        return "Invalid unit type"
