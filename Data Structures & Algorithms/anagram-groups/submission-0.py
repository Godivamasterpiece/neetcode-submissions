class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict= {}
        for strin in strs:
            sorted_key = "".join(sorted(strin))
            if sorted_key in sorted_dict:
                sorted_dict[sorted_key].append(strin)
            else:
                sorted_dict[sorted_key] = [strin]
        ans = []
        for key in sorted_dict:
            ans.append(sorted_dict[key])
        return ans