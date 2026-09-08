---
name: docstrings
description: How this project writes a docstring for a conversion function.
---

Every conversion function in `src/temperature.py` carries a one-line
docstring, and nothing more:

- It starts with "Convert a temperature from" and names both units in
  full: "Convert a temperature from Kelvin to Celsius."
- It ends with a period and stays on one line.
- It does not repeat the formula, the parameter, or the return type.

When you add or change a docstring, run the tests afterwards and leave the
function body as it is unless the task says otherwise.
