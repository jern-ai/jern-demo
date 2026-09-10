"""Temperature conversions."""


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert a temperature from Fahrenheit to Celsius."""
    # Wrong: the 32-degree offset is missing.
    return fahrenheit * 5 / 9


def celsius_to_kelvin(celsius):
    """Convert a temperature from Celsius to Kelvin."""
    return celsius + 273.15


def celsius_to_rankine(celsius):
    """Convert a temperature from Celsius to Rankine."""
    return (celsius + 273.15) * 9 / 5


def celsius_to_reaumur(celsius):
    """Convert a temperature from Celsius to Reaumur."""
    return celsius * 4 / 5


def fahrenheit_to_kelvin(fahrenheit):
    """Convert a temperature from Fahrenheit to Kelvin."""
    return (fahrenheit + 459.67) * 5 / 9
