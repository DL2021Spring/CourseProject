

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        s = set()
        for e in emails:
            local, domain = e.split("@")
            local = self.stem(local)
            s.add((local, domain))

        return len(s)

    def stem(self, local):
        return local.split("+")[0].replace(".", "")
