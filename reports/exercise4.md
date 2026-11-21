# Bug reports for exercise4.py

Line: 7
Problem: The docstring says the function should return true if the password is the admin password, but the code returns true only if the password is equal to ADMIN_PASSWORD and ADMIN_PASSWORD is not empty. Since ADMIN_PASSWORD is hardcoded and non-empty, the condition "ADMIN_PASSWORD != """ is always true, making the function effectively return password == "admin123". This is a logical error because it does not correctly reflect the intent of checking if the password is the admin password. Additionally, the function will return True for any password matching "admin123", which is correct, but the condition is unnecessarily complex and could be simplified.
Example: check_admin("admin123") returns True, which is correct, but check_admin("") returns True, which is wrong because an empty password should not be considered the admin password.
Fix: return password == ADMIN_PASSWORD

Line: 14
Problem: The function builds a SQL query with user input directly in an f-string, which allows SQL injection. An attacker can provide malicious input like "'; DROP TABLE users; --" to execute arbitrary SQL commands.
Example: find_user(db, "'; DROP TABLE users; --") could drop the users table.
Fix: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
