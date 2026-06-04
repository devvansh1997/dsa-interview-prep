class Solution:
    def findMin(self, nums: List[int]) -> int:
        # result
        result = nums[0]

        # counters
        l, r = 0, len(nums)-1

        while l <= r:
            # if already inside sorted portion -> just look at left for min
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            
            # mid calc
            mid = (l + r) // 2
            result = min(result, nums[mid])

            # condition: is our mid part of the left sorted portion -> look at right
            if nums[mid] >= nums[l]:
                l = mid + 1
            # condition: nope, part of right -> look at left sorted portion
            else:
                r = mid - 1

        return result