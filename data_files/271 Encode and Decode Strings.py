
__author__ = 'Daniel'


class Codec(object):
    def encode(self, strs):
        
        strs = map(lambda x: str(len(x))+"/"+x, strs)
        return reduce(lambda x, y: x+y, strs, "")  

    def decode(self, s):
        
        strs = []
        i = 0
        while i < len(s):
            j = s.index("/", i)
            l = int(s[i:j])
            strs.append(s[j+1:j+1+l])
            i = j+1+l

        return strs


class CodecMethod2(object):
    def encode(self, strs):
        
        strs = map(lambda x: x.replace("\n", "\n\n")+"_\n_", strs)
        return reduce(lambda x, y: x+y, strs, "")

    def decode(self, s):
        
        strs = s.split("_\n_")
        strs = strs[:-1]  
        return map(lambda x: x.replace("\n\n", "\n"), strs)


class CodecError(object):
    def encode(self, strs):
        
        strs = map(lambda x: x.replace("\x00", "\\x00"), strs)
        ret = ""
        for s in strs:
            ret += s+"\x00"
        return ret

    def decode(self, s):
        
        if "\x00" not in s:
            return []

        s = s[:-1]  
        strs = s.split("\x00")
        strs = map(lambda x: x.replace("\\x00", "\x00"), strs)
        return strs
