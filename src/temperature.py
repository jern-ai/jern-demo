"""Temperature conversions."""


def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert a Fahrenheit temperature to Celsius."""
    # Wrong: the 32-degree offset is missing.
    return fahrenheit * 5 / 9
