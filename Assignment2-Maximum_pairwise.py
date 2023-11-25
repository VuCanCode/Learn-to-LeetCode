import numpy as np

class Solution():
    """
    Find maximum pairwise product from an array of non-negative number
    """
    def find_maximum_pairwise_product(self, nums) -> int:
        max_num_1 = 0
        max_num_2 = 0
        current_num = 0
        for i in range(len(nums)):
            current_num = nums[i]
            if current_num > max_num_1:
                max_num_2 = max_num_1
                max_num_1 = current_num
            elif current_num > max_num_2:
                max_num_2 = current_num

        return max_num_2 * max_num_1

if __name__ == "__main__":
    nums_size = input()
    inputs = input()
    nums = list(map(int, inputs.split()))
    print(nums)
    Sol = Solution()
    print(Sol.find_maximum_pairwise_product(nums))

                
