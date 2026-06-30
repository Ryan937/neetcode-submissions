class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()

        for email in emails:
            curr = email.split("@")
            local_name = curr[0].split("+")[0].replace(".", "")
            new_email = local_name + curr[1]

            if new_email not in seen:
                seen.add(new_email)

        return len(seen)