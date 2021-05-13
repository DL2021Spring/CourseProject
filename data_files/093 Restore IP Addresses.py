
__author__ = 'Danyang'


class Solution:
    def restoreIpAddresses(self, s):
        
        result = []
        self.dfs(s, [], result)
        return result

    def dfs_complicated(self, seq, cur, result):
        
        if len(cur) > 4:
            return

        if not cur or self.is_valid(cur[-1]):
            if len(cur) == 4 and not seq:  
                result.append(".".join(cur))
                return

            for i in xrange(1, min(3, len(seq))+1):
                self.dfs(seq[i:], cur+[seq[:i]], result)

    def dfs(self, seq, cur, result):
        
        
        if not seq and len(cur)==4:
            result.append(".".join(cur))
            return

        
        
        for i in xrange(1, min(3, len(seq)) + 1):
            new_seg = seq[:i]
            
            if len(cur) < 4 and self.is_valid(new_seg):
                self.dfs(seq[i:], cur + [new_seg], result)
            else:
                return

    def is_valid(self, s):
        if not s:
            return False
        return s == "0" or s[0]!="0" and 0<= int(s) <256  

if __name__=="__main__":
    IP = "25525511135"
    print Solution().restoreIpAddresses(IP)
