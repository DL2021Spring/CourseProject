
__author__ = 'Danyang'


def bitFlip(cipher):
    
    if len(cipher) <= 2:
        return len(cipher)

    cipher = [val if val == 1 else -1 for val in cipher]

    
    maxl = 0
    maxr = -1
    min_sum = 1 << 31

    ssum = 0
    l = 0
    r = -1

    for ind, val in enumerate(cipher):
        ssum += val
        if ssum > 0:
            l = ind + 1
            r = ind
            ssum = 0

        if ssum < 0:
            r = ind

        if min_sum > ssum:
            min_sum = ssum
            maxr, maxl = r, l

    cipher = [val if val == 1 else 0 for val in cipher]
    for i in xrange(maxl, maxr + 1):
        cipher[i] ^= 1

    return sum(cipher)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    N = int(f.readline().strip())

    cipher = []
    for t in xrange(N):
        
        i = int(f.readline().strip())
        cipher.append(i)
        
    s = "%s\n" % (bitFlip(cipher))
    print s,
