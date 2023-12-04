# #%%
# # Naive Method O(N)
# class Solution():
#     def find_last_digit_of_sum(self, n):
#         first = 0
#         sec = 1
#         result = 0
#         for i in range(1, n):
#             first %= 10
#             sec %= 10
#             fib_last = first + sec
#             result += fib_last
#             first = sec
#             sec = fib_last

#         return (result + 1) % 10

# if __name__ == "__main__":
#     sol = Solution()
#     n = int(input())
#     print(sol.find_last_digit_of_sum(n))

# %%
# More Efficient Method
class Solution():
    def find_last_digit_of_sum(self, n):
        pisano_len = 60

        n %= pisano_len
        if n <= 2:
            return n
        first = 0
        sec = 1
        result = 0
        for i in range(n):
            fib = first + sec
            first = sec
            sec = fib
            result += first

        return (result) % 10
    
if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    print(sol.find_last_digit_of_sum(n))

        

# %%
