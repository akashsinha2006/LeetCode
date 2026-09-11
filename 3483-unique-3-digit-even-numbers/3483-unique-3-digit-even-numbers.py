class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()

        for a in range(1, 10):
            for b in range(10):
                for c in range(0, 10, 2):
                    arr = digits.copy()

                    for x in [a, b, c]:
                        if x in arr:
                            arr.remove(x)
                        else:
                            break
                    else:
                        ans.add(a * 100 + b * 10 + c)

        return len(ans)