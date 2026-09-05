"""Lookup table mapping every temperature scale pair to a conversion function.

Each entry maps a ``(source, target)`` pair to the callable that converts a
value from the source scale to the target scale.
"""

from typing import Callable, Dict, Tuple

from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

Converter = Callable[[float], float]

CONVERSIONS: Dict[Tuple[str, str], Converter] = {
    ("celsius", "fahrenheit"): celsius_to_fahrenheit,
    ("fahrenheit", "celsius"): fahrenheit_to_celsius,
}


def get_converter(source: str, target: str) -> Converter:
    """Return the conversion function for a source/target scale pair.

    Args:
        source: Name of the scale to convert from.
        target: Name of the scale to convert to.

    Returns:
        The callable that converts ``source`` values into ``target`` values.

    Raises:
        KeyError: If no conversion is defined for the scale pair.
    """
    return CONVERSIONS[(source, target)]
