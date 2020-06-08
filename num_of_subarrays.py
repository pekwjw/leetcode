class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        count = 0
        sum_slide = sum(arr[0:k])
        ts = threshold * k

        for i in range(len(arr)-k+1):
            if sum_slide >= ts:
                count += 1
            if i < len(arr)-k:
                sum_slide = sum_slide-arr[i]+arr[i+k]
        return count

print Solution().numOfSubarrays([2,2,2,2,5,5,5,8],3,4)
