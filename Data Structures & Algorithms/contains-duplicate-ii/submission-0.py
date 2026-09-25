class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myset = set()
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r] in myset:
                return True
            myset.add(nums[r])
            if r - l >= k:
                myset.remove(nums[l])
                l += 1
        return False