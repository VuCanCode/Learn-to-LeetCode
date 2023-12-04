# %%
# More Efficient Method
class Solution():
    def find_last_digit_of_sum(self, m, n):
        pisano_len = 60
        n %= pisano_len
        m %= pisano_len
        if n < m:
            n += 60

        first = 0
        sec = 1
        result = 0
        for i in range(n + 1):            
            if i >= m:
                result += first
            fib = first + sec
            first = sec
            sec = fib


        return (result) % 10
    
if __name__ == "__main__":
    sol = Solution()
    m, n = map(int, input().split())
    print(sol.find_last_digit_of_sum(m, n))

# %%
