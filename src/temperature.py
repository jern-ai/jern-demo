"""Temperature conversions."""


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    # Wrong: the 32-degree offset is missing.
    return fahrenheit * 5 / 9
