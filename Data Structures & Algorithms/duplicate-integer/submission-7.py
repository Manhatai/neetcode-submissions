class Solution:
    def hasDuplicate(self, list):
        seen = set()
        for x in range(len(list)):
            if list[x] in seen:
                return True
            seen.add(list[x])
        return False
