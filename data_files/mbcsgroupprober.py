




























from .charsetgroupprober import CharSetGroupProber
from .utf8prober import UTF8Prober
from .sjisprober import SJISProber
from .eucjpprober import EUCJPProber
from .gb2312prober import GB2312Prober
from .euckrprober import EUCKRProber
from .big5prober import Big5Prober
from .euctwprober import EUCTWProber


class MBCSGroupProber(CharSetGroupProber):
    def __init__(self):
        CharSetGroupProber.__init__(self)
        self._mProbers = [
            UTF8Prober(),
            SJISProber(),
            EUCJPProber(),
            GB2312Prober(),
            EUCKRProber(),
            Big5Prober(),
            EUCTWProber()
        ]
        self.reset()
