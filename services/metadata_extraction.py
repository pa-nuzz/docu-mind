import re

def extract_metadata(text: str) -> dict:
    """
    Extract basic metadata from text using regex.
    Assumes document is a resume or invoice.
    """

    # Email pattern
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    email_match = re.search(email_pattern, text)

    # Phone number pattern (simple, not perfect)
    phone_pattern = r"\+?\d[\d\s\-]{8,}\d"
    phone_match = re.search(phone_pattern, text)

    return {
        "email": email_match.group() if email_match else None,
        "phone": phone_match.group() if phone_match else None
    }
