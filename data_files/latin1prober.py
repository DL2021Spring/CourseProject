



























from .charsetprober import CharSetProber
from .constants import eNotMe
from .compat import wrap_ord

FREQ_CAT_NUM = 4

UDF = 0  
OTH = 1  
ASC = 2  
ASS = 3  
ACV = 4  
ACO = 5  
ASV = 6  
ASO = 7  
CLASS_NUM = 8  

Latin1_CharToClass = (
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, ASC, ASC, ASC, ASC, ASC, ASC, ASC,   
    ASC, ASC, ASC, ASC, ASC, ASC, ASC, ASC,   
    ASC, ASC, ASC, ASC, ASC, ASC, ASC, ASC,   
    ASC, ASC, ASC, OTH, OTH, OTH, OTH, OTH,   
    OTH, ASS, ASS, ASS, ASS, ASS, ASS, ASS,   
    ASS, ASS, ASS, ASS, ASS, ASS, ASS, ASS,   
    ASS, ASS, ASS, ASS, ASS, ASS, ASS, ASS,   
    ASS, ASS, ASS, OTH, OTH, OTH, OTH, OTH,   
    OTH, UDF, OTH, ASO, OTH, OTH, OTH, OTH,   
    OTH, OTH, ACO, OTH, ACO, UDF, ACO, UDF,   
    UDF, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, ASO, OTH, ASO, UDF, ASO, ACO,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    ACV, ACV, ACV, ACV, ACV, ACV, ACO, ACO,   
    ACV, ACV, ACV, ACV, ACV, ACV, ACV, ACV,   
    ACO, ACO, ACV, ACV, ACV, ACV, ACV, OTH,   
    ACV, ACV, ACV, ACV, ACV, ACO, ACO, ACO,   
    ASV, ASV, ASV, ASV, ASV, ASV, ASO, ASO,   
    ASV, ASV, ASV, ASV, ASV, ASV, ASV, ASV,   
    ASO, ASO, ASV, ASV, ASV, ASV, ASV, OTH,   
    ASV, ASV, ASV, ASV, ASV, ASO, ASO, ASO,   
)





Latin1ClassModel = (
    
    0,  0,  0,  0,  0,  0,  0,  0,  
    0,  3,  3,  3,  3,  3,  3,  3,  
    0,  3,  3,  3,  3,  3,  3,  3,  
    0,  3,  3,  3,  1,  1,  3,  3,  
    0,  3,  3,  3,  1,  2,  1,  2,  
    0,  3,  3,  3,  3,  3,  3,  3,  
    0,  3,  1,  3,  1,  1,  1,  3,  
    0,  3,  1,  3,  1,  1,  3,  3,  
)


class Latin1Prober(CharSetProber):
    def __init__(self):
        CharSetProber.__init__(self)
        self.reset()

    def reset(self):
        self._mLastCharClass = OTH
        self._mFreqCounter = [0] * FREQ_CAT_NUM
        CharSetProber.reset(self)

    def get_charset_name(self):
        return "windows-1252"

    def feed(self, aBuf):
        aBuf = self.filter_with_english_letters(aBuf)
        for c in aBuf:
            charClass = Latin1_CharToClass[wrap_ord(c)]
            freq = Latin1ClassModel[(self._mLastCharClass * CLASS_NUM)
                                    + charClass]
            if freq == 0:
                self._mState = eNotMe
                break
            self._mFreqCounter[freq] += 1
            self._mLastCharClass = charClass

        return self.get_state()

    def get_confidence(self):
        if self.get_state() == eNotMe:
            return 0.01

        total = sum(self._mFreqCounter)
        if total < 0.01:
            confidence = 0.0
        else:
            confidence = ((self._mFreqCounter[3] / total)
                          - (self._mFreqCounter[1] * 20.0 / total))
        if confidence < 0.0:
            confidence = 0.0
        
        
        confidence = confidence * 0.5
        return confidence
