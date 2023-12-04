"""
Generate the nth number in the fibonacci sequence
"""

class Solution():
    def find_nth_fib(self, n: int):
        first = 0
        sec = 1
        if n < 1:
            return n
        for i in range(n):
            sum = first + sec
            first = sec
            sec = sum
        return first


if __name__ == "__main__":
    n = int(input())
    sol = Solution()
    print(sol.find_nth_fib(n))