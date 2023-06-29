class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        res = set()

        for email in emails:

            email, domain = email.split("@")
            email = email.split("+")[0]
            tmp = ""
            for c in email:
                if c == ".":
                    continue
                tmp += c
            res.add((tmp, domain))

        return len(res)


