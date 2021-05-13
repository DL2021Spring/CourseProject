
__author__ = 'Danyang'
class Solution:
    def countAndSay(self, n):
        
        string = "1"
        for i in range(1, n):
            string = self.singleCountAndSay(string)
        return string


    def singleCountAndSay(self, num_string):
        
        string_builder = ""

        i = 0
        while i<len(num_string):
            
            j = i+1
            while j<len(num_string) and num_string[j]==num_string[i]:
                j += 1
            count = j-i
            string_builder += str(count)+str(num_string[i])
            i = j

        return string_builder

if __name__=="__main__":
    print Solution().countAndSay(4)