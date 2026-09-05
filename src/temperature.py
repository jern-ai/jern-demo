"""Temperature conversions."""

import os


def get_pgdatabase():
    return os.environ.get("PGDATABASE")


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
