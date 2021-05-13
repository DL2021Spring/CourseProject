



















__author__ = 'Tim Wegener <twegener@radlogic.com.au>'
__date__ = '$Date: 2007/03/27 03:15:06 $'
__version__ = '$Revision: 0.45 $'
__credits__ = 

import re
import sys
import time
import random

try:
    True, False
except NameError:
    True, False = (1==1, 0==1)


def int2bin(i, n):
    
    hex2bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
               '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
               'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
    
    result = ''.join([hex2bin[x] for x in hex(i).lower().replace('l','')[2:]])
                      
    
    
    if '1' in result[:-n]:
        raise ValueError("Value too large for given number of bits.")
    result = result[-n:]
    
    result = '0'*(n-len(result)) + result
    return result


def bin2int(bin_string):
    










    return int(bin_string, 2)


def reverse(input_string):
    
    str_list = list(input_string)
    str_list.reverse()
    return ''.join(str_list)


def transpose(matrix):
    
    result = zip(*matrix)
    
    
    
    result = map(list, result)
    return result


def polygon_area(points_list, precision=100):
    
    
    for i in range(len(points_list)):
        points_list[i] = (int(points_list[i][0] * precision),
                          int(points_list[i][1] * precision))
    
    if points_list[-1] != points_list[0]:
        points_list.append(points_list[0])
    
    area = 0
    for i in range(len(points_list)-1):
        (x_i, y_i) = points_list[i]
        (x_i_plus_1, y_i_plus_1) = points_list[i+1]
        area = area + (x_i_plus_1 * y_i) - (y_i_plus_1 * x_i)
    area = abs(area / 2)
    
    area = float(area)/(precision**2)
    return area


def timestamp():
    

    return time.asctime()


def pt2str(point):
    
    return "(%s, %s)" % (str(point[0]), str(point[1]))


def gcf(a, b, epsilon=1e-16):
    
    result = max(a, b)
    remainder = min(a, b)
    while remainder and abs(remainder) > epsilon:
        new_remainder = result % remainder
        result = remainder
        remainder = new_remainder
    return abs(result)

def lcm(a, b, precision=None):
    
    
    
    
    denom = gcf(a, b)
    if denom == 0:
        result = 0
    else:
        result = a * (b / denom)
    return result


def permutations(input_list):
    
    out_lists = []
    if len(input_list) > 1:
        
        item = input_list[0]
        
        sub_lists = permutations(input_list[1:])
        
        for sub_list in sub_lists:
            
            for i in range(len(input_list)):
                new_list = sub_list[:]
                new_list.insert(i, item)
                out_lists.append(new_list)
    else:
        
        out_lists = [input_list]
    return out_lists


def reduce_fraction(fraction):
    
    (numerator, denominator) = fraction
    common_factor = abs(gcf(numerator, denominator))
    result = (numerator/common_factor, denominator/common_factor)
    return result


def quantile(l, p):
    
    l_sort = l[:]
    l_sort.sort()
    n = len(l)
    r = 1 + ((n - 1) * p)
    i = int(r)
    f = r - i
    if i < n:
        result =  (1-f)*l_sort[i-1] + f*l_sort[i]
    else:
        result = l_sort[i-1]
    return result


def trim(l):
    
    l_sort = l[:]
    l_sort.sort()
    
    if len(l_sort) % 2 == 0:
        
        index = int(len(l_sort) / 2)  
        median = float(l_sort[index] + l_sort[index-1]) / 2
    else:
        
        index = int(len(l_sort) / 2)
        median = l_sort[index]
    
    q1 = quantile(l_sort, 0.25)
    q3 = quantile(l_sort, 0.75)
    iqr = q3 - q1
    iqr_extra = iqr * 1.5
    def in_interval(x, i=iqr_extra, q1=q1, q3=q3):
        return (x >= q1-i and x <= q3+i)
    l_trimmed = [x for x in l_sort if in_interval(x)]
    return l_trimmed


def nice_units(value, dp=0, sigfigs=None, suffix='', space=' ',
               use_extra_prefixes=False, use_full_name=False, mode='si'):
    
    si_prefixes = {1e24:  ('Y', 'yotta'),
                   1e21:  ('Z', 'zetta'),
                   1e18:  ('E', 'exa'),
                   1e15:  ('P', 'peta'),
                   1e12:  ('T', 'tera'),
                   1e9:   ('G', 'giga'),
                   1e6:   ('M', 'mega'),
                   1e3:   ('k', 'kilo'),
                   1e-3:  ('m', 'milli'),
                   1e-6:  ('u', 'micro'),
                   1e-9:  ('n', 'nano'),
                   1e-12: ('p', 'pico'),
                   1e-15: ('f', 'femto'),
                   1e-18: ('a', 'atto'),
                   1e-21: ('z', 'zepto'),
                   1e-24: ('y', 'yocto')
                   }
    if use_extra_prefixes:
        si_prefixes.update({1e2:  ('h', 'hecto'),
                            1e1:  ('da', 'deka'),
                            1e-1: ('d', 'deci'),
                            1e-2: ('c', 'centi')
                            })
    bin_prefixes = {2**10: ('K', 'kilo'),
                    2**20: ('M', 'mega'),
                    2**30: ('G', 'mega'),
                    2**40: ('T', 'tera'),
                    2**50: ('P', 'peta'),
                    2**60: ('E', 'exa')
                    }
    if mode == 'bin':
        prefixes = bin_prefixes
    else:
        prefixes = si_prefixes
    prefixes[1] = ('', '')  
    
    multipliers = prefixes.keys()
    multipliers.sort()
    mult = None
    for i in range(len(multipliers) - 1):
        lower_mult = multipliers[i]
        upper_mult = multipliers[i+1]
        if lower_mult <= value < upper_mult:
            mult_i = i
            break
    if mult is None:
        if value < multipliers[0]:
            mult_i = 0
        elif value >= multipliers[-1]:
            mult_i = len(multipliers) - 1
    mult = multipliers[mult_i]
    
    new_value = value / mult
    
    if sigfigs is None:
        if mult_i < (len(multipliers) - 1) and \
               round(new_value, dp) == \
               round((multipliers[mult_i+1] / mult), dp):
            mult = multipliers[mult_i + 1]
            new_value = value / mult
    
    if use_full_name:
        label_type = 1
    else:
        label_type = 0
    
    if sigfigs is None:
        str_value = eval('"%.'+str(dp)+'f" % new_value', locals(), {})
    else:
        str_value = eval('"%.'+str(sigfigs)+'g" % new_value', locals(), {})
    return str_value + space + prefixes[mult][label_type] + suffix


def uniquify(seq, preserve_order=False):
    
    try:
        
        d = {}
        if preserve_order:
            
            
            return [x for x in seq if (x not in d) and not d.__setitem__(x, 0)]
        else:
            for x in seq:
                d[x] = 0
            return d.keys()
    except TypeError:
        
        result = []
        app = result.append
        for x in seq:
            if x not in result:
                app(x)
        return result


unique = uniquify


def reverse_dict(d):
    
    result = {}
    for key, value in d.items():
        result[value] = key
    return result

    
def lsb(x, n):
    
    return x & ((2 ** n) - 1)


def gray_encode(i):
    

    return i ^ (i >> 1)


def random_vec(bits, max_value=None):
    

    vector = ""
    for _ in range(int(bits / 10) + 1):
        i = int((2**10) * random.random())
        vector += int2bin(i, 10)

    if max_value and (max_value < 2 ** bits - 1):
        vector = int2bin((int(vector, 2) / (2 ** bits - 1)) * max_value, bits)
    
    return vector[0:bits]


def binary_range(bits):
    
    l = []
    v = ['0'] * bits

    toggle = [1] + [0] * bits
    
    while toggle[bits] != 1:
        v_copy = v[:]
        v_copy.reverse()
        l.append(''.join(v_copy))
        
        toggle = [1] + [0]*bits
        i = 0
        while i < bits and toggle[i] == 1:
            if toggle[i]:
                if v[i] == '0':
                    v[i] = '1'
                    toggle[i+1] = 0
                else:
                    v[i] = '0'
                    toggle[i+1] = 1
            i += 1
    return l


def float_range(start, stop=None, step=None):
    
    if stop is None:
        stop = float(start)
        start = 0.0

    if step is None:
        step = 1.0

    cur = float(start)
    l = []
    while cur < stop:
        l.append(cur)
        cur += step

    return l


def find_common_fixes(s1, s2):
    
    prefix = []
    suffix = []

    i = 0
    common_len = min(len(s1), len(s2))
    while i < common_len:
        if s1[i] != s2[i]:
            break

        prefix.append(s1[i])
        i += 1

    i = 1
    while i < (common_len + 1):
        if s1[-i] != s2[-i]:
            break
        
        suffix.append(s1[-i])
        i += 1

    suffix.reverse()

    prefix = ''.join(prefix)
    suffix = ''.join(suffix)
        
    return (prefix, suffix)


def is_rotated(seq1, seq2):
    
    
    if len(seq1) != len(seq2):
        return False
    
    start_indexes = []
    head_item = seq2[0]
    for index1 in range(len(seq1)):
        if seq1[index1] == head_item:
            start_indexes.append(index1)
    
    double_seq1 = seq1 + seq1
    for index1 in start_indexes:
        if double_seq1[index1:index1+len(seq1)] == seq2:
            return True
    return False

def getmodule(obj):
    
    if hasattr(obj, 'func_globals'):
        func = obj
    else:
        
        func = None
        for item in obj.__dict__.values():
            if hasattr(item, 'func_globals'):
                func = item
                break
        if func is None:
            raise ValueError("No functions attached to object: %r" % obj)
    module_name = func.func_globals['__name__']
    
    module = sys.modules[module_name]
    return module


def round_grid(value, grid, mode=0):
    
    off_grid = value % grid
    if mode == 0:
        add_one = int(off_grid >= (grid / 2.0))
    elif mode == 1 and off_grid:
        add_one = 1
    elif mode == -1 and off_grid:
        add_one = 0
    result = ((int(value / grid) + add_one) * grid)
    return result


def get_args(argv):
    
    d = {}
    args = []
    
    for arg in argv:
            
        if arg.startswith('-'):
            parts = re.sub(r'^-+', '', arg).split('=')
            if len(parts) == 2:
                d[parts[0]] = parts[1]
            else:
                d[parts[0]] = None
        else:
            args.append(arg)

    d['args'] = args
    
    return d


if __name__ == '__main__':
    import doctest
    doctest.testmod(sys.modules['__main__'])

