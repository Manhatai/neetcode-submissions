class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listOfSChars: list[list[str]] = []
        listOfTChars: list[list[str]] = []

        for i in range(len(s)):
            if [s[i]] in listOfSChars:
                listOfSChars[listOfSChars.index([s[i]])].append(s[i])
            else:
                listOfSChars.append([s[i]])

        for i in range(len(t)):
            if [t[i]] in listOfTChars:
                listOfTChars[listOfTChars.index([t[i]])].append(t[i])
            else:
                listOfTChars.append([t[i]])

        return sorted(listOfSChars) == sorted(listOfTChars)