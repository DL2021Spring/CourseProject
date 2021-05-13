
__author__ = 'Daniel'


class Solution:
    def replaceBlank(self, string, length):
        
        i = 0
        while i < length:
            if string[i] == " ":
                string.append("")
                string.append("")
                length += 2
                for j in xrange(length-1, i, -1):
                    string[j] = string[j-2]

                string[i:i+3] = list("%20")
                i += 2
            i += 1

        return length

if __name__ == "__main__":
    assert Solution().replaceBlank(list("Mr John Smith"), 13) == 17