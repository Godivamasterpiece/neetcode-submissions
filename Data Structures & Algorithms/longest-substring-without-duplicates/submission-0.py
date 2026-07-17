class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen, left = 0,0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            maxlen = max(maxlen, right - left + 1)
        
        return maxlen