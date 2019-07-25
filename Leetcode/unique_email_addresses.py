def plus_format(email: str) -> str:
    if ('+' in email):
        plus_index = email.index('+')
        at_index = email.index('@')
        return email[:plus_index] + email[at_index:]
    else:
        return email

def dot_format(email: str) -> str:
    fragmented_email = email.split('@')
    fragmented_email[0] = fragmented_email[0].replace('.','')
    return '@'.join(fragmented_email)

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        formatted_emails = [ dot_format(plus_format(email)) for email in emails ]
        return len(set(formatted_emails))
