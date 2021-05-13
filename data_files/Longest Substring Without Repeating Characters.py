
__author__ = 'Daniel'


class Solution:
    def lengthOfLongestSubstring(self, s):
        b = 0
        e = 0
        n = len(s)
        maxa = 0
        st = set()  
        while e < n:
            while s[e] in st:
                st.remove(s[b])
                b += 1

            st.add(s[e])
            e += 1
            maxa = max(maxa, e-b)

        return maxa

if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3





