
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
                result.append("."".""j""o""i""n""(""c""u""r"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""1"","" ""m""i""n""(""3"","" ""l""e""n""(""s""e""q"")"")""+""1"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""f""s""(""s""e""q""[""i"":""]"","" ""c""u""r""+""[""s""e""q""["":""i""]""]"","" ""r""e""s""u""l""t"")""
""
"" "" "" "" ""d""e""f"" ""d""f""s""(""s""e""l""f"","" ""s""e""q"","" ""c""u""r"","" ""r""e""s""u""l""t"")"":""
"" "" "" "" "" "" "" "" 
        
        if not seq and len(cur)==4:
            result.append("."".""j""o""i""n""(""c""u""r"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n""
""
"" "" "" "" "" "" "" "" ""#"" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""1"","" ""3""+""1"")"":""
"" "" "" "" "" "" "" "" ""#"" ""f""o""r"" ""l""o""o""p""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""1"","" ""m""i""n""(""3"","" ""l""e""n""(""s""e""q"")"")"" ""+"" ""1"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""n""e""w""_""s""e""g"" ""="" ""s""e""q""["":""i""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""c""o""n""d""i""t""i""o""n"" ""c""h""e""c""k""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""l""e""n""(""c""u""r"")"" ""<"" ""4"" ""a""n""d"" ""s""e""l""f"".""i""s""_""v""a""l""i""d""(""n""e""w""_""s""e""g"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""f""s""(""s""e""q""[""i"":""]"","" ""c""u""r"" ""+"" ""[""n""e""w""_""s""e""g""]"","" ""r""e""s""u""l""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n""
""
"" "" "" "" ""d""e""f"" ""i""s""_""v""a""l""i""d""(""s""e""l""f"","" ""s"")"":""
"" "" "" "" "" "" "" "" ""i""f"" ""n""o""t"" ""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""F""a""l""s""e""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s"" ""=""="" 