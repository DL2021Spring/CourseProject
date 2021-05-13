
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        cipher = cipher[0]
        length = len(cipher)
        if length & 1 == 1:
            return -1
        str1 = cipher[:length / 2]
        str2 = cipher[length / 2:]
        
        
        
        
        
        
        
        

        
        bucket = [0 for _ in xrange(256)]
        for elt in str1:
            bucket[ord(elt)] += 1
        for elt in str2:
            bucket[ord(elt)] -= 1
        return sum(filter(lambda x: x > 0, bucket))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = f.readline().strip().split(' ')

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
