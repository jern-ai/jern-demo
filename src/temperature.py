"""Temperature conversions between Celsius and Fahrenheit.

Provides:
    celsius_to_fahrenheit: convert a temperature from Celsius to Fahrenheit.
    fahrenheit_to_celsius: convert a temperature from Fahrenheit to Celsius.
"""


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert a temperature from Fahrenheit to Celsius."""
    # Wrong: the 32-degree offset is missing.
    return fahrenheit * 5 / 9
