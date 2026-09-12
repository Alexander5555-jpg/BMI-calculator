#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2026 Alexander Bartek <dev.alexander3892@proton.me>
# SPDX-License-Identifier: GPL-3.0-or-later

"""
    BMI-calculator: Simple BMI calculator from weight and height input.

    Copyright (C) 2026 Alexander Bartek <dev.alexander3892@proton.me>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

def main():
    weight_input = input("Enter your weight in kilograms:\n")
    weight = weight_to_float(weight_input)
    print()
    height_input = input("Now enter your height in centimeters:\n")
    height = height_to_float(height_input)
    print()
    print(f"Your BMI is: {bmi_value(weight, height):.1f}")

    
def weight_to_float(w):
    w = w.rstrip("kg")
    w = float(w)
    return w




def height_to_float(h):
    h = h.rstrip("cm")
    h = float(h)
    return h / 100




def bmi_value(weight, height):
    return weight / (height * height)





main()
