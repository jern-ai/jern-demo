"""Temperature conversions."""


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_rankine(celsius):
    return celsius * 9 / 5 + 491.67
