class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap
        anagram_map = defaultdict(list)
        
        # sort each word in strs
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        # return the values back
        return list(anagram_map.values())