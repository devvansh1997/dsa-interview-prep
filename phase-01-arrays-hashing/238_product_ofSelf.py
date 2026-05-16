class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # setup prefix and suffix arrays
        prefix = [1 for _ in range(len(nums))]
        suffix = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):                # i = 1, 2, ..., n-1
            prefix[i] = prefix[i-1] * nums[i-1]

        for j in range(len(nums)-2, -1, -1):         # j = n-2, n-3, ..., 0
            suffix[j] = suffix[j+1] * nums[j+1]
        
        return [prefix[i] * suffix[i] for i in range(len(nums))]
