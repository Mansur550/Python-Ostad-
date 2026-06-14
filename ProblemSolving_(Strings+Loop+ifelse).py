"""
1. 🔒 Mask Sensitive Data (NID/ID)

Hide part of sensitive information.
"""

nid = "1234567890"

masked = nid[:2] + "*" * 6 + nid[8:]
print(masked)