class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        # sort the array
        nums.sort()

        # two-sum problem keeping one number at a time fixed
        for idx, n in enumerate(nums):
            if idx != 0 and nums[idx] == nums[idx-1]:
                continue
            # setup up current array
            i, j = idx+1, len(nums)-1
            two_sum = 0
            target = -nums[idx] 
            while i < j:
                # calculate total sum
                two_sum = nums[i] + nums[j]
                # if sum is greater then we decrease the right pointer 
                if two_sum < target:
                    i += 1
                # else the left pointer
                elif two_sum > target:
                    j -= 1
                # we found an answer
                else:
                    answer.append([nums[idx], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                    
        return answer