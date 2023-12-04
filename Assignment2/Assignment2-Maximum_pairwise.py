
class Solution():
    """
    Find maximum pairwise product from an array of non-negative number
    """
    def find_maximum_pairwise_product(self, nums) -> int:
        max_num_1 = 0
        max_num_2 = 0
        for i in range(len(nums)):
            if nums[i] > max_num_1:
                max_num_1 = nums[i]
                index = i
        for i in range(len(nums)):
            if nums[i] > max_num_2 and index != i:
                max_num_2 = nums[i]
        return max_num_2 * max_num_1

if __name__ == "__main__":
    nums_size = input()
    inputs = input()
    nums = list(map(int, inputs.split()))
    Sol = Solution()
    print(Sol.find_maximum_pairwise_product(nums))

                
