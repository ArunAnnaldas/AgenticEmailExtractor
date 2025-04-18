import re

def extract_emails_from_json(json_data):
    emails = set()
    email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    def extract_recursive(obj):
        if isinstance(obj, dict):
            for value in obj.values():
                extract_recursive(value)
        elif isinstance(obj, list):
            for item in obj:
                extract_recursive(item)
        elif isinstance(obj, str):
            found = re.findall(email_regex, obj)
            emails.update(found)

    for item in json_data:
        extract_recursive(item)

    return list(emails)
