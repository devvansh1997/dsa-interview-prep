class Solution:
    def isPalindrome(self, s: str) -> bool:
        reduced_string = ''
        # remove delimiters or special characters
        for char in s.lower():
            if char.isalnum():
                reduced_string += char.lower()
        
        i, j = 0, len(reduced_string)-1
        while i != j and i < j:
            if reduced_string[i] == reduced_string[j]:
                i += 1
                j -= 1
            else:
                # print(f"s[i] = {s[i]} | s[j] = {s[j]}")
                return False
        return True