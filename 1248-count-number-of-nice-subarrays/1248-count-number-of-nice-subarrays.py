class Solution:
    def numberOfSubarrays(self, nums, k):
        count = {0: 1}
        odd = 0
        ans = 0

        for num in nums:
            odd += num % 2

            if odd - k in count:
                ans += count[odd - k]

            count[odd] = count.get(odd, 0) + 1

        return ans