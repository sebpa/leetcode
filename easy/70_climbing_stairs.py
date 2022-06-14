from functools import cache


class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs_2(self, n: int) -> int:
        if n <= 2:
            return n
        two_step_before, step_before = 1, 2
        current = 0
        for i in range(3, n + 1):
            current = step_before + two_step_before
            two_step_before, step_before = step_before, current
        return current


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(1000))
    print(solution.climbStairs_2(1000))