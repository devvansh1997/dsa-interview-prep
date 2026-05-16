class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        # build count map
        count_map = defaultdict(int)
        for n in nums:
            count_map[n] += 1

        # build buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count_map.items():
            buckets[freq].append(num)
        
        i = len(nums)
        while i >= 0 and k > 0:
            if buckets[i]:
                answer.extend(buckets[i])
                k -= len(buckets[i])
            i -= 1
        return answer