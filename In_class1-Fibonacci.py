# First Attempt

# result = [0, 1]
# class Solution():
#     def recursive(self, num, first = 0, second = 1):
#         sum = first + second
#         if sum < num:
#             result.append(sum)
#             self.recursive(num, second, sum)

# if __name__ == "__main__":
#     num = int(input())
#     sol = Solution()
#     sol.recursive(num = num)
#     print(result)
#%%
"""
Find the ith Number in the fibonacci series
"""
# Naive Method
# def recur(num):
#     if num <= 1:
#         return num
#     else:
#         return recur(num - 1) + recur(num - 2)

# if __name__ == "__main__":
#     num = int(input("Input a number "))
#     print(recur(num))
#     print("done")

# %%
# Efficient method
# My Attempt
array = [0, 1]
def find_Fib(num):
    if num <= 1:
        return num
    for i in range(num):
        sum = array[-1] + array[-2]
        array.append(sum)
    return sum

if __name__ == "__main__":
    num = int(input("Input a number "))
    print(find_Fib(num))

