class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)

        def check(length):
            seen = set()

            for i in range(n-length + 1):
                sub = s[i:i + length]
                if sub in seen:
                    return sub
                seen.add(sub)
            return ""
        left, right = 1, n-1
        answer = ""

        while left <= right:
            mid = (left + right) //2
            sub = check(mid)

            if sub :
                answer = sub
                left = mid+1
            else:
                right = mid -1
        return answer