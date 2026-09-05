class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        sorted_freq = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return [num for num, count in sorted_freq[:k]]

        