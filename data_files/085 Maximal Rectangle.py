
__author__ = 'Danyang'


class Solution:
    def maximalRectangle(self, matrix):
        
        if not matrix or not matrix[0]:
            return 0

        

        global_max = -1<<32
        m = len(matrix)
        n = len(matrix[0])

        
        dp_height = [[-1 for _ in xrange(n)] for _ in xrange(m)]
        dp_height[0] = map(lambda x: int(x), matrix[0])
        for i in xrange(1, m):
            for j in xrange(n):
                if matrix[i][j] == "1"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""d""p""_""h""e""i""g""h""t""[""i""]""[""j""]"" ""="" ""1""+""d""p""_""h""e""i""g""h""t""[""i""-""1""]""[""j""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""d""p""_""h""e""i""g""h""t""[""i""]""[""j""]"" ""="" ""0""
""
"" "" "" "" "" "" "" "" ""#"" ""e""n""d"" ""o""f"" ""d""p""
""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""m"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""L""a""r""g""e""s""t"" ""R""e""c""t""a""n""g""l""e"" ""i""n"" ""H""i""s""t""o""g""r""a""m""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""n""c""_""s""t""a""c""k"" ""="" ""[""]""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""j"" ""="" ""0""
"" "" "" "" "" "" "" "" "" "" "" "" ""w""h""i""l""e"" ""j""<""=""n"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""i""f"" ""n""o""t"" ""i""n""c""_""s""t""a""c""k"" ""o""r"" ""j""+""1""<""n"" ""a""n""d"" ""d""p""_""h""e""i""g""h""t""[""i""]""[""j""]""<""=""d""p""_""h""e""i""g""h""t""[""i""]""[""j""+""1""]"":"" "" ""#"" ""m""i""s""t""a""k""e""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""n""o""t"" ""i""n""c""_""s""t""a""c""k"" ""o""r"" ""j""<""n"" ""a""n""d"" ""d""p""_""h""e""i""g""h""t""[""i""]""[""j""]"">""=""d""p""_""h""e""i""g""h""t""[""i""]""[""i""n""c""_""s""t""a""c""k""[""-""1""]""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""n""c""_""s""t""a""c""k"".""a""p""p""e""n""d""(""j"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""j"" ""+""="" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""l""a""s""t"" ""="" ""i""n""c""_""s""t""a""c""k"".""p""o""p""("")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""h""e""i""g""h""t"" ""="" ""s""e""l""f"".""g""e""t""_""h""e""i""g""h""t""(""m""a""t""r""i""x"","" ""i"","" ""l""a""s""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""h""e""i""g""h""t"" ""="" ""d""p""_""h""e""i""g""h""t""[""i""]""[""l""a""s""t""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""i""n""c""_""s""t""a""c""k"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""g""l""o""b""a""l""_""m""a""x"" ""="" ""m""a""x""(""g""l""o""b""a""l""_""m""a""x"","" ""h""e""i""g""h""t""*""(""j""-""(""i""n""c""_""s""t""a""c""k""[""-""1""]""+""1"")"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""g""l""o""b""a""l""_""m""a""x"" ""="" ""m""a""x""(""g""l""o""b""a""l""_""m""a""x"","" ""h""e""i""g""h""t""*""j"")""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""g""l""o""b""a""l""_""m""a""x""
""
"" "" "" "" ""d""e""f"" ""g""e""t""_""h""e""i""g""h""t""(""s""e""l""f"","" ""m""a""t""r""i""x"","" ""r""o""w"","" ""c""o""l"")"":""
"" "" "" "" "" "" "" "" ""#"" ""p""o""s""s""i""b""l""e"" ""r""e""p""l""a""c""e"" ""b""y"" ""d""p"";"" ""o""t""h""e""r""w""i""s""e"" ""T""L""E""
"" "" "" "" "" "" "" "" ""h""e""i""g""h""t"" ""="" ""0""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""r""o""w"","" ""-""1"","" ""-""1"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""m""a""t""r""i""x""[""r""o""w""]""[""c""o""l""]"" ""=""="" 