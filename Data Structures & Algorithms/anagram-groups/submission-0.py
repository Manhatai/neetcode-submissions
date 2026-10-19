class Solution:
    def groupAnagrams(self, anagramsList: list[str]):
        seen: dict[str, list[str]] = {}

        for string in anagramsList:
            key = "".join(sorted(string))

            if key in seen:
                seen[key].append(string)
            else:
                seen[key] = [string]

        return list(seen.values())

        