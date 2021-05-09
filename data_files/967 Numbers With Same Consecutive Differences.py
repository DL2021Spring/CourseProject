

from typing import List


class Solution:
    def __init__(self):
        self.cache = {}

    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        
        ret = []
        for i in range(1, 10):
            ret.extend(self.dfs(i, N, K))

        if N == 1:
            ret.append([0])  

        return list(
            map(lambda x: int("".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""x"")"")"")"","" ""r""e""t"")""
"" "" "" "" "" "" "" "" "")""
""
"" "" "" "" ""d""e""f"" ""d""f""s""(""s""e""l""f"","" ""s""t""a""r""t"":"" ""i""n""t"","" ""N"":"" ""i""n""t"","" ""K"":"" ""i""n""t"")"" ""-"">"" ""L""i""s""t""[""L""i""s""t""[""i""n""t""]""]"":""
"" "" "" "" "" "" "" "" ""i""f"" ""(""s""t""a""r""t"","" ""N"","" ""K"")"" ""n""o""t"" ""i""n"" ""s""e""l""f"".""c""a""c""h""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"" ""="" ""[""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""N"" ""=""="" ""1"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"" ""="" ""[""[""s""t""a""r""t""]""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""i""f"" ""N"" "">"" ""1"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""s""t""a""r""t"" ""+"" ""K"" ""<""="" ""9"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""e"" ""i""n"" ""s""e""l""f"".""d""f""s""(""s""t""a""r""t"" ""+"" ""K"","" ""N"" ""-"" ""1"","" ""K"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"".""a""p""p""e""n""d""(""[""s""t""a""r""t""]"" ""+"" ""e"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""s""t""a""r""t"" ""-"" ""K"" "">""="" ""0"" ""a""n""d"" ""K"" ""!""="" ""0"":"" "" ""#"" ""s""p""e""c""i""a""l"" ""c""a""s""e""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""e"" ""i""n"" ""s""e""l""f"".""d""f""s""(""s""t""a""r""t"" ""-"" ""K"","" ""N"" ""-"" ""1"","" ""K"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"".""a""p""p""e""n""d""(""[""s""t""a""r""t""]"" ""+"" ""e"")""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""c""a""c""h""e""[""s""t""a""r""t"","" ""N"","" ""K""]"" ""="" ""r""e""t""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""c""a""c""h""e""[""s""t""a""r""t"","" ""N"","" ""K""]""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 