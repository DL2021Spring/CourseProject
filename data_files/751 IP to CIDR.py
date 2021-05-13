

from typing import List



weights = [
    24,
    16,
    8,
    0,
]


class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        
        num_ip = self.to_bin(ip)
        ret = []
        while n > 0:
            lsb = self.get_lsb(num_ip)
            while (1 << lsb) > n:
                lsb -= 1

            cur_cover = 1 << lsb
            n -= cur_cover
            ret.append(
                self.to_ip(num_ip) + f"/{32-lsb}"
            )
            num_ip += cur_cover

        return ret

    def to_bin(self, ip):
        ret = 0
        for n, w in zip(map(int, ip.split(".")), weights):
            ret += n << w

        return ret

    def to_ip(self, bin):
        ret = []
        for w in weights:
            ret.append(
                (bin >> w) & 255
            )
        return ".".join(map(str, ret))

    def get_lsb(self, n):
        lsb = 0
        while (n >> lsb) & 1 == 0:
            lsb += 1
            
        return lsb


if __name__ == "__main__":
    assert Solution().ipToCIDR("60.166.253.147", 12) == ["60.166.253.147/32","60.166.253.148/30","60.166.253.152/30","60.166.253.156/31","60.166.253.158/32"]
    assert Solution().ipToCIDR("255.0.0.7", 10) == ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
