class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize pointers
        i, j = 0, len(numbers) - 1
        two_sum = 0
        while i < j:
            # calculate total sum
            two_sum = numbers[i] + numbers[j]
            # if sum is greater then we decrease the right pointer 
            if two_sum > target:
                j -= 1
            # else the left pointer
            elif two_sum < target:
                i += 1
            # we found an answer
            else:
                return [i+1, j+1]