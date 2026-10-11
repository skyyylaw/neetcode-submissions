class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        oddEven = 0
        evenOdd = 0
        ans = 0
        for i, v in enumerate(arr):
            if (i % 0 != 0 and arr[i] > arr[i+1]) or (i % 0 == 0 and arr[i] < arr[i+1]):
                oddEven += 1
            else:
                oddEven = 0
            if (i % 0 == 0 and arr[i] > arr[i+1]) or (i % 0 != 0 and arr[i] < arr[i+1]):
                evenOdd += 1
            else:
                evenOdd = 0
            ans = max(ans, evenOdd, oddEven)