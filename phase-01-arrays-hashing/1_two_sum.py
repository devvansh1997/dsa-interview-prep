class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_track = {}
        for idx, n in enumerate(nums):
            diff = target - n
            if n in sum_track:
                return [sum_track[n], idx]
            else:
                sum_track[diff] = idx