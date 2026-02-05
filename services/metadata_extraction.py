# import re
#
# def extract_metadata(text: str) -> dict:
#     """
#     Extract basic metadata from document text.
#     """
#
#     email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
#     phone_pattern = r"\+?\d[\d\s\-]{8,}\d"
#
#     email_match = re.search(email_pattern, text)
#     phone_match = re.search(phone_pattern, text)
#
#     return {
#         "email": email_match.group().lower() if email_match else None,
#         "phone": phone_match.group() if phone_match else None
#     }

import re

def extract_metadata(text: str) -> dict:
    
    # Extract email and phone from raw text.
    # Includes simple OCR correction for common email mistakes.


    # Common OCR fixes for emails
    fixed_text = text

    # fix gmail-like mistakes
    fixed_text = re.sub(r'(\w)rgigmail\.com', r'\1@gmail.com', fixed_text)
    fixed_text = re.sub(r'(\w)gmail\.com', r'\1@gmail.com', fixed_text)

    # email regex
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"\+?\d[\d\s\-]{8,}\d"

    email_match = re.search(email_pattern, fixed_text)
    phone_match = re.search(phone_pattern, fixed_text)

    return {
        "email": email_match.group().lower() if email_match else None,
        "phone": phone_match.group() if phone_match else None
    }
