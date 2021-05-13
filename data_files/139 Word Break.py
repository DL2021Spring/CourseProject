
__author__ = 'Danyang'
class Solution:
    def wordBreak_TLE(self, s, dict):
        
        string_builder = ""
        if s=="":
            return True

        
        for i in range(len(s)):
            string_builder += s[i]
            if string_builder in dict:
                try:
                    if self.wordBreak_TLE(s[i+1:], dict):
                        return True
                    else:
                        continue
                except IndexError:
                    return True

        return False

    def wordBreak(self, s, dict):
        
        dp = [False] * (len(s)+1)
        dp[0] = True 

        for i in range(len(dp)):  
            
            if dp[i]:
                for word in dict:
                    try:
                        
                        if dp[i+len(word)]==True:
                            continue

                        
                        if s[i:i+len(word)]==word: 
                            dp[i+len(word)] = True  
                    except IndexError:
                        continue

        return dp[-1]



if __name__=="__main__":
    assert Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"])==True