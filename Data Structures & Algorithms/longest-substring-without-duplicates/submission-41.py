class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        l_index = 0
        r_index = 1
        current_len = 0
        max_len = 0
        while r_index <= len(s):
            window_set = set(char for char in s[l_index:r_index])
            if len(s[l_index:r_index]) > len(window_set):
                l_index += 1
                current_len -= 1
            else:
                r_index += 1
                current_len += 1
                if current_len > max_len:
                    max_len = current_len
        return max_len
