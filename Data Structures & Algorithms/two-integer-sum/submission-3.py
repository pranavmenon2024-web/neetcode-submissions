class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check={}
        for i, num in enumerate(nums):
            check[num]=i
        for i, num in enumerate(nums):
            comp=target-num
            if comp in check and check[comp] != i:
                return [i, check[comp]]
        return []
            

