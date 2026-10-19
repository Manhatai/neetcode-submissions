class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen: dict[int, int] = {}

        for i in nums: 
            if i in seen:
                seen[i] = seen[i] + 1
            else:
                seen[i] = 0

        sorted_seen = sorted(seen, key=seen.get, reverse=True)

        return sorted_seen[:k]

