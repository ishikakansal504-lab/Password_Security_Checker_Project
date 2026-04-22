import string
import math
from getpass import getpass
import sys

password = getpass("Enter your password: ")

if not password:
    print("Password cannot be empty!")
    sys.exit(1)

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in string.punctuation for c in password)

score = 0
feedback = []

if len(password) < 8:
    feedback.append("Use at least 8 characters")
else:
    score += 1

if not has_upper:
    feedback.append("Add uppercase letter")
else:
    score += 1

if not has_lower:
    feedback.append("Add lowercase letter")
else:
    score += 1

if not has_digit:
    feedback.append("Add a number")
else:
    score += 1

if not has_special:
    feedback.append("Add special character (!@#$%)")
else:
    score += 1

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
elif score == 5 and len(password) >= 12:
    strength = "Very Strong"
else:
    strength = "Strong"

charset = 0
if has_lower: charset += 26
if has_upper: charset += 26
if has_digit: charset += 10
if has_special: charset += len(string.punctuation)
entropy = len(password) * math.log2(charset) if charset else 0

common_passwords = ["123456", "password", "qwerty", "abc123", "admin", "letmein"]
common_warning = "Very common password - avoid!" if password.lower().strip() in common_passwords else ""

print("\n--- Password Analysis ---")
print(f"Strength: {strength} (Score: {score}/5)")
print(f"Entropy: {entropy:.2f} bits")
if common_warning:
    print(common_warning)

if feedback:
    print("Suggestions:")
    for f in feedback:
        print(f" - {f}")
else:
    print("Great job! Bulletproof password.")