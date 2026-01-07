import re

def is_exit_command(text):
    exit_keywords = ["bye", "exit", "quit", "thank you", "thanks"]
    return text.lower().strip() in exit_keywords

def validate_email(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email)

def validate_phone(phone):
    pattern = r"^[0-9]{10}$"
    return re.match(pattern, phone)
