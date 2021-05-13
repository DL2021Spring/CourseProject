
__author__ = 'Danyang'


class Solution:
    def hashCode(self, key, HASH_SIZE):
        
        w = 1
        ret = 0
        for i in xrange(len(key)-1, -1, -1):
            ret = (ret+ord(key[i])*w)%HASH_SIZE
            w = (w*33)%HASH_SIZE
        return ret


if __name__ == "__main__":
    assert Solution().hashCode("abcd", 100) == 78

