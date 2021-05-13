
__author__ = 'Danyang'


class Solution:
    def convert(self, s, nRows):
        
        length = len(s)
        matrix = [[] for _ in xrange(nRows)]

        i = 0
        while i < length:
            try:
                
                for j in xrange(nRows):
                    matrix[j].append(s[i])
                    i += 1

                
                for j in xrange(nRows-1-1, 0, -1):
                    matrix[j].append(s[i])
                    i += 1

            except IndexError:
                break

        lst = ["".join(element) for element in matrix]
        return "".join(lst)


if __name__ == "__main__":
    assert Solution().convert("ABCD", 2) == "ACBD