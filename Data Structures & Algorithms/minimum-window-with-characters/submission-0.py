class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        need_led = len(need)
        formed = 0
        window = {}
        res = ""
        left = 0
        res_len = float('inf')

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in need and window[char] == need[char]:
                formed += 1
            # print(formed)
            while formed == need_led:
                # print("Reducing Window")
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res = s[left:right+1]
                # print(res)
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return res