class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')] * n
        left = 0
        total = 0
        ans = float('inf')
        minimum = float('inf')

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                if left > 0:
                    ans = min(ans, length + best[left - 1])

                minimum = min(minimum, length)

            best[right] = minimum

        return -1 if ans == float('inf') else ans