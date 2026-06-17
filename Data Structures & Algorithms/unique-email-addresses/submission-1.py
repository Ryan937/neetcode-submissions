class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = 0
        seen = set()

        for email in emails:
            curr = email.split("@")
            local_name = curr[0].split("+")[0].replace(".", "")
            new_email = local_name + curr[1]

            print(new_email)
            
            if new_email not in seen:
                seen.add(new_email)
                result += 1       

        return result