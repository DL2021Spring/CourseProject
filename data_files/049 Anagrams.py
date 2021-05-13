
__author__ = 'Danyang'
class Solution:
    def anagrams_complicated(self, strs):
        
        temp = list(strs)
        for ind, string in enumerate(temp):
            if string and string!="":  
                string = [char for char in string]
                string.sort()
                string = "".join(string)
                temp[ind] = string


        hash_map = {}
        for ind, string in enumerate(temp):
            indexes = hash_map.get(string, [])
            indexes.append(ind)  
            hash_map[string] = indexes

        result = []
        for val in hash_map.values():
            if len(val)>1:
                
                result += [strs[i] for i in val]
        return result

    def anagrams(self, strs):
        
        hash_map = {}
        for ind, string in enumerate(strs):
            string = "".join(sorted(string))  
            if string not in hash_map:
                hash_map[string] = [ind]
            else:
                hash_map[string].append(ind)
            
            
            

        result = []
        for val in hash_map.values():
            if len(val)>1:
                
                result += [strs[i] for i in val]
        return result

if __name__=="__main__":
    Solution().anagrams(["", ""])