# Bug reports for exercise1.py

Line: 3
Problem: The docstring says the function should return True for even numbers, but the code checks if n % 2 == 1, which is true for odd numbers, not even ones.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: The docstring states the function should return the area of a rectangle, which is width times height, but the code returns the sum of width and height.
Example: rectangle_area(3, 4) returns 7, expected 12.
Fix: return width * height

Line: 13
Problem: The docstring says the function should return twice the number n, but the code returns n + 2, which is not twice the number.
Example: double(5) returns 7, expected 10.
Fix: return n * 2
