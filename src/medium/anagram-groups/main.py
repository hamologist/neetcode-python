class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        memo: dict[str, list[str]] = {}

        for entry in strs:
            check = [0] * 26
            for char in entry:
                check[ord(char) - 97] += 1
            
            key = ','.join([str(x) for x in check])
            if key not in memo:
                memo[key] = []
            
            memo[key].append(entry)

        result = []
        for group in memo.values():
            result.append(group)

        return result
