class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            r = num % k
            new_dp[r] += 1

            for old_r in range(k):
                if dp[old_r]:
                    new_r = (old_r * r) % k
                    new_dp[new_r] += dp[old_r]

            dp = new_dp


            for r in range(k):
                ans[r] += dp[r]

        return ans