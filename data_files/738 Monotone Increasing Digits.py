



class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        
        digits = [int(e) for e in str(N)]
        pointer = len(digits)
        for i in range(len(digits) - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                pointer = i
                digits[i - 1] -= 1

        for i in range(pointer, len(digits)):
            digits[i] = 9

        return int("".join(map(str, digits)))


if __name__ == "__main__":
    assert Solution().monotoneIncreasingDigits(10) == 9
    assert Solution().monotoneIncreasingDigits(332) == 299
