class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        a = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        starts = [x[0] for x in a]

        nxt = [bisect_right(starts, a[i][1]) for i in range(n)]

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for k in range(1, 5):
                skip = dp[i + 1][k]
                s, ids = dp[nxt[i]][k - 1]
                take = (s + a[i][2], tuple(sorted(ids + (a[i][3],))))

                dp[i][k] = max(skip, take, key=lambda x: (x[0], tuple(-j for j in x[1])))

        return list(dp[0][4][1])