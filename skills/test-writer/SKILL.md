# Test writer

You receive ONE bug report and the Python file it refers to.
Write ONE test that proves the bug.

The test must FAIL on the current buggy code and PASS once the bug is fixed.

OUTPUT RULES:
- Output ONLY Python code. No explanations, no markdown, no code fences.
- Exactly one function, and its name starts with test_
- Do NOT write any import. The functions of the file are already imported.
- Use one concrete assert, for example:

def test_is_adult_at_18():
    assert is_adult(18) == True

INPUT RULES (very important):
- First read the docstring of the function in the file. Ignore the Example
  line of the bug report if it breaks any rule of the docstring.
- Your input must satisfy EVERY condition of the docstring except the one
  that the bug breaks.
- If the docstring mentions a digit, the input string MUST contain a digit,
  for example "abcdefg1" (exactly 8 characters, with a digit).
- Never use "abcdefgh" or any password without a digit when the docstring
  asks for a digit.
- The expected value comes from the docstring, not from the buggy code.
- Test the boundary exactly: for a minimum of 8 characters, use exactly 8.
