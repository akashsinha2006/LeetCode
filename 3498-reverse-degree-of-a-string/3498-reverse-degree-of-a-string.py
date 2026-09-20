class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0

        for i, ch in enumerate(s,1):
            value = ord('z') - ord(ch) +1
            total += value * i
        return total