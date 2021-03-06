


import linecache
import random


class ReadFile(object):
    def __init__(self, pth1, num=None):
        self.pth1 = pth1
        self.num = num
        linecache.clearcache()
        self.total = int(linecache.getline(pth1, 1))
        if num == None:
            self.num = self.total

    def __get_line_label(self, tmp, rand):
        if rand:
            line_label = random.sample(tmp, self.num)
        else:
            line_label = tmp[:self.num]
        return line_label

    def person_pair(self):
        person = []
        tmp = range(2, self.total + 2)

        
        if self.num != self.total:
            
            line_label = self.__get_line_label(tmp, False)

            for i in line_label:
                person.append(self.__extract_flnm(i))
        
        else:
            for i in tmp:
                person.append(self.__extract_flnm(i))

        return person

    def person_mispair(self):
        person = []
        tmp = range(self.total + 2, self.total * 2 + 2)

        if self.num != self.total:
            
            line_label = random.sample(tmp, self.num)  

            for i in range(len(line_label)):
                person.append(self.__extract_flnm(line_label[i]))
        else:
            for i in tmp:
                person.append(self.__extract_flnm(i))

        return person

    def __extract_flnm(self, line_label):
        tmp = linecache.getline(self.pth1, line_label)
        tmp = tmp.split()
        suffix = '.txt'  

        if len(tmp) == 3:
            flag = 1
            fl_nm1 = tmp[0] + '_' + '0'*(4 - len(tmp[1])) + tmp[1] + suffix
            fl_nm2 = tmp[0] + '_' + '0'*(4 - len(tmp[2])) + tmp[2] + suffix
        else:
            flag = -1
            fl_nm1 = tmp[0] + '_' + '0'*(4 - len(tmp[1])) + tmp[1] + suffix
            fl_nm2 = tmp[2] + '_' + '0'*(4 - len(tmp[3])) + tmp[3] + suffix

        pair_info = [fl_nm1, fl_nm2, flag]

        return pair_info
