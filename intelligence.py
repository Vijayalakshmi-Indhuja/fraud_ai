# intelligence.py

import re

def extract_intelligence(text: str):

    # Bank account numbers (9–18 digit sequences)
    bank_accounts = re.findall(r"\b\d{9,18}\b", text)

    # UPI IDs (example@bank)
    upi_ids = re.findall(r"\b[\w\.-]+@[\w]+\b", text)

    # URLs (http or https)
    urls = re.findall(r"https?://[^\s]+", text)

    return {
        "bank_accounts": list(set(bank_accounts)),
        "upi_ids": list(set(upi_ids)),
        "phishing_links": list(set(urls))
    }
