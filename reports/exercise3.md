# Bug reports for exercise3.py

Line: 3
Problem: The function crashes on an empty list because len(numbers) is 0, leading to division by zero, but the docstring states that an empty list has an average of 0.
Example: average([]) raises ZeroDivisionError, expected 0.
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8
Problem: The function returns the first word of the text, but if the text is empty or has no words (e.g., "   "), split() returns an empty list, and accessing [0] raises an IndexError. The docstring says it returns "" if the text is empty.
Example: first_word("   ") returns IndexError, expected "".
Fix: return text.split()[0] if text.split() else ""

Line: 12
Problem: The function returns part / total * 100, which crashes with ZeroDivisionError when total is 0, but the docstring specifies that if total is 0, the result is 0.
Example: percent(5, 0) raises ZeroDivisionError, expected 0.
Fix: return part / total * 100 if total != 0 else 0
