ransomNote="aa"
magazine="aab"

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDict = {}
        for char in magazine:
            if char not in magazineDict:
                magazineDict[char] = 1
            else:
                magazineDict[char] += 1

        for char in ransomNote:
            if char not in magazineDict or magazineDict[char] == 0:
                return False
            else:
                magazineDict[char] -= 1
        return True
print(Solution().canConstruct(ransomNote,magazine))