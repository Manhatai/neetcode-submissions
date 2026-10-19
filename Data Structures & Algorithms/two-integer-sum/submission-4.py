class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        possibleSolutions: list[list[int]] = []

        # if sum(nums) < target:
        #     return 

        for i in range(target + 1):
            possibleSolutions.append([i, target - i])

        for solution in possibleSolutions:
            try:
                index0 = nums.index(solution[0])
                index1 = nums.index(solution[1], index0 + 1)
                print(index0, index1)
                return [index0, index1]
            except ValueError:
                continue