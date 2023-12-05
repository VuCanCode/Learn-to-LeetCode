# %%
# More Efficient Method
class Solution():
    def find_last_digit_of_sum_of_square(self, n):
        pisano_len = 60
        n %= pisano_len
        first = 0
        sec = 1
        result = 0
        for i in range(n + 1):            
            result += first**2
            fib = first + sec
            first = sec
            sec = fib


        return (result) % 10
    
if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    print(sol.find_last_digit_of_sum_of_square(n))

    # %%
