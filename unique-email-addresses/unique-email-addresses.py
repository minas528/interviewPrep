class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            first = email.split('@')[0]
            second = email.split('@')[1]
            first = first.split('+')[0]
            first = first.replace('.', '')
            s.add(first+'@'+second)
        print(s)
        return len(s)