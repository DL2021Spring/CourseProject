
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, M, ppl = cipher
        team_cnt = 0
        max_topic = 0
        for i in xrange(N):
            for j in xrange(i + 1, N):
                cnt = self.common_topics(M, ppl[i], ppl[j])
                if cnt == max_topic:
                    team_cnt += 1
                elif cnt > max_topic:
                    team_cnt = 1
                    max_topic = cnt
        return "%d\n%d" % (max_topic, team_cnt)

    def common_topics(self, M, a, b):
        topic = a | b
        topic_cnt = bin(topic).count("1")  
        
        
        
        
        
        return topic_cnt


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    N, M = map(lambda x: int(x), f.readline().strip().split(" "))
    ppl = []
    for i in xrange(N):
        ppl.append(int(f.readline().strip(), 2))

    cipher = [N, M, ppl]
    s = "%s\n" % (Solution().solve(cipher))
    print s,
