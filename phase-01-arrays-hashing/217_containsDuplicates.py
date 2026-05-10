class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_dict = {}
        for n in nums:
            if n in check_dict:
                return True
            else:
                check_dict[n] = 1
        return False  