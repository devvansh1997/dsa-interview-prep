class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # setup return encoded message
        encoding_string = ''
        for s in strs:
            length = len(s)
            encoding_string += str(length) + '#' + s
        return encoding_string

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        decoded_strs = []
        i = 0
        # look at each character
        while i < len(str):
            j = i
            while str[j] != '#':       # find the '#'
                j += 1
            length = int(str[i:j])     # the digits between i and j
            word   = str[j+1 : j+1+length]
            decoded_strs.append(word)
            i = j + 1 + length       # jump past the word
            
        return decoded_strs
