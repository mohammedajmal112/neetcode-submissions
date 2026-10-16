class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repeating_map = {}
        for num in nums:
            if num not in repeating_map:
                repeating_map[num] = []
            repeating_map[num].append(num)
        sorted_val = sorted(repeating_map.values(), key=len, reverse=True)
        result_arr = []
        for i in range(k):
            result_arr.append(sorted_val[i][0])
        result_arr.sort()
        return result_arr
