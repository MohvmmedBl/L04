# Bug reports for exercise2.py

Line: 3
Problem: The docstring says "True if the grade is 5 or more", but the code uses > 5, which means grades of 5 are False, not True.
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: The docstring says "At least 8 characters", but the code uses > 8, which means passwords with exactly 8 characters are rejected.
Example: is_valid_password("abcdefgh") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: The code returns max(low, min(x, low)), which simplifies to low regardless of x, so it always returns low, not clamped between low and high.
Example: clamp(10, 5, 20) returns 5, expected 10.
Fix: return max(low, min(x, high))
