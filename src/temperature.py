"""Temperature conversions between Celsius and Fahrenheit.

Provides:
- celsius_to_fahrenheit: convert a Celsius value to Fahrenheit.
- fahrenheit_to_celsius: convert a Fahrenheit value to Celsius.
"""


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
