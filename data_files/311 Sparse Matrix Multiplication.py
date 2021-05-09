
__author__ = 'Daniel'


class Solution(object):
    def multiply(self, A, B):
        
        m, n = len(A), len(A[0])
        A1 = [{} for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if A[i][j] != 0:
                    A1[i][j] = A[i][j]

        m, n = len(B), len(B[0])
        B1 = [{} for _ in xrange(n)]
        for i in xrange(m):
            for j in xrange(n):
                if B[i][j] != 0:
                    B1[j][i] = B[i][j]

        ret = [[0 for _ in xrange(len(B[0]))] for _ in xrange(len(A))]
        for i, row in enumerate(A1):
            for j, col in enumerate(B1):
                s = 0
                for k in row.keys():
                    if k in col:
                        s += row[k]*col[k]
                ret[i][j] = s

        return ret

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""A"" ""="" ""[""
"" "" "" "" "" "" "" "" ""[""1"","" ""0"","" ""0""]"",""
"" "" "" "" "" "" "" "" ""[""-""1"","" ""0"","" ""3""]""
"" "" "" "" ""]""
""
"" "" "" "" ""B"" ""="" ""[""
"" "" "" "" "" "" "" "" ""[""7"","" ""0"","" ""0""]"",""
"" "" "" "" "" "" "" "" ""[""0"","" ""0"","" ""0""]"",""
"" "" "" "" "" "" "" "" ""[""0"","" ""0"","" ""1""]""
"" "" "" "" ""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""u""l""t""i""p""l""y""(""A"","" ""B"")"" ""=""="" ""[""[""7"","" ""0"","" ""0""]"","" ""[""-""7"","" ""0"","" ""3""]""]""
""
