class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # not the same len = cannot be anagram
        if len(s) != len(t):
            return False

        # define dicts
        s_map, t_map = {}, {}

        for idx, val in enumerate(s):
            # s_map
            if val not in s_map:
                s_map[val] = 1
            else: s_map[val] += 1
        
        for idx, val in enumerate(t):
            # t_map
            if val not in t_map:
                t_map[val] = 1
            else: t_map[val] += 1
        
        return True if (s_map == t_map) else False