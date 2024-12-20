# Vessel Hydrodynamics Project

## Overview
Welcome to the Vessel Hydrodynamics Project, a school project and basic Python program designed to compute key hydrodynamic properties of vessels such as the Froude number and hydrodynamic lift, while allowing users to input various characteristics of their vessel.

## Features

- **Color Selection:** Prompts the user to select a vessel color from a predefined list.
- **Vessel Type:** Determines whether the vessel is classified as a "Boat" or "Ship" based on its weight.
- **Unit Conversions:** Provides conversions between feet and meters, and knots to meters per second.
- **Hydrodynamic Lift Calculation:** Computes the Froude number and categorizes the hydrodynamic lift of the vessel into one of three levels: 
  - Negligible hydrodynamic lift
  - Negative hydrodynamic lift
  - Hydrodynamic lift represents 50% of the displacement
- **Validation:** Ensures the user input is valid and within specified ranges.

## Functions

- `get_color()`: Prompts the user to select a vessel color (1 for Red, 2 for Blue, 3 for White).
- `ship_or_boat()`: Prompts the user to input the weight of the vessel and determines whether it is a "Boat" or "Ship".
- `feet_to_meter(feet)`: Converts a given length in feet to meters.
- `knot_to_meter_sec(knots)`: Converts a given velocity in knots to meters

