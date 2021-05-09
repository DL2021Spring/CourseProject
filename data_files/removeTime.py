import re
import os

texts = []

directory = os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(directory):
	for file in files:
		if file.endswith("."s"r"t"")"":""
""	""	""	""f""=""o""p""e""n""(""o""s"".""p""a""t""h"".""j""o""i""n""(""r""o""o""t"",""f""i""l""e"")"","" ""'""r""'"")""
""	""	""	""t""e""x""t""s"".""a""p""p""e""n""d""(""(""f""i""l""e"",""f"".""r""e""a""d""("")"")"")""
""	""	""	""f"".""c""l""o""s""e""("")""
""
""p""1"" ""="" ""r""e"".""c""o""m""p""i""l""e""(""(""'""^""\""d""+""$""'"")"")""
""p""2"" ""="" ""r""e"".""c""o""m""p""i""l""e""(""(""'""\""d""\""d"":""\""d""\""d"":""\""d""\""d""'"")"")""
""
""f""o""r"" ""v""i""d""e""o""N""a""m""e"","" ""v""i""d""e""o""T""e""x""t""s"" ""i""n"" ""t""e""x""t""s"":""
""	""t""r""a""n""s""c""r""i""p""t""s"" ""="" ""'""'""
""	""l""i""n""e""s"" ""="" ""v""i""d""e""o""T""e""x""t""s"".""s""p""l""i""t""l""i""n""e""s""("")""
""	""f""o""r"" ""l""i""n""e"" ""i""n"" ""l""i""n""e""s"":""
""	""	""i""f"" ""n""o""t"" ""(""p""1"".""s""e""a""r""c""h""(""l""i""n""e"")"" ""o""r"" ""p""2"".""s""e""a""r""c""h""(""l""i""n""e"")"" ""o""r"" ""l""e""n""(""l""i""n""e"")"" ""<"" ""1"")"":""
""	""	""	""t""r""a""n""s""c""r""i""p""t""s"" ""+""="" ""(""l""i""n""e""+""'""\""n""'"")""
""	""f"" ""="" ""o""p""e""n""(""v""i""d""e""o""N""a""m""e""["":""l""e""n""(""v""i""d""e""o""N""a""m""e"")""-""4""]""+""'""_""c""l""e""a""n""e""d"".""t""x""t""'"",""'""w""'"")""
""	""f"".""w""r""i""t""e""(""t""r""a""n""s""c""r""i""p""t""s"")""
""	""p""r""i""n""t""(""v""i""d""e""o""N""a""m""e"" ""+"" ""'"" ""h""a""s"" ""b""e""e""n"" ""c""l""e""a""n""e""d"".""'"")""
""	""f"".""c""l""o""s""e""("")""
""
""#""f""i""l""e""N""a""m""e"" ""="" ""'""J""e""l""l""y"" ""R""o""l""l"" ""I""c""e"" ""C""r""e""a""m"" ""B""o""m""b""e"" ""R""e""c""i""p""e"" ""-"" ""L""a""u""r""a"" ""V""i""t""a""l""e"" ""-"" ""L""a""u""r""a"" ""i""n"" ""t""h""e"" ""K""i""t""c""h""e""n"" ""E""p""i""s""o""d""e"" ""7""9""0"" ""[""E""n""g""l""i""s""h""]""-""4"".""t""x""t""'""
""
""#"" ""#"" ""f"" ""="" ""o""p""e""n""(""f""i""l""e""N""a""m""e"",""'""r""'"")""
""
""#"" ""p""1"" ""="" ""r""e"".""c""o""m""p""i""l""e""(""(""'""^""\""d""+""$""'"")"")""
""#"" ""p""2"" ""="" ""r""e"".""c""o""m""p""i""l""e""(""(""'""\""d""\""d"":""\""d""\""d"":""\""d""\""d""'"")"")""
""
""#"" ""t""r""a""n""s""c""r""i""p""t""s"" ""="" ""'""'""
""
""#"" ""#"" ""t""e""x""t"" ""="" ""f"".""r""e""a""d""("")"".""s""p""l""i""t""l""i""n""e""s""("")""
""#"" ""#"" ""f"".""c""l""o""s""e""("")""
""
""#"" ""f""o""r"" ""l""i""n""e"" ""i""n"" ""t""e""x""t"":""
""#"" ""	""i""f"" ""n""o""t""(""p""1"".""s""e""a""r""c""h""(""l""i""n""e"")"" ""o""r"" ""p""2"".""s""e""a""r""c""h""(""l""i""n""e"")"" ""o""r"" ""l""e""n""(""l""i""n""e"")"" ""<"" ""1"")"":""
""#"" ""	""	""t""r""a""n""s""c""r""i""p""t""s""+""=""(""l""i""n""e""+""'""\""n""'"")""
""
""#"" ""f""2"" ""="" ""o""p""e""n""(""f""i""l""e""N""a""m""e""+""'""-""c""l""e""a""n""e""d"".""t""x""t""'"",""'""a""'"")""
""#"" ""f""2"".""w""r""i""t""e""(""t""r""a""n""s""c""r""i""p""t""s"")""
""#"" ""f""2"".""c""l""o""s""e""("")