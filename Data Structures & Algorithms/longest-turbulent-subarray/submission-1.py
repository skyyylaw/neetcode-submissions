class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        oddEven = 0
        evenOdd = 0
        ans = 0
        for i in range(len(arr)):
            if i == len(arr) - 1:
                if oddEven > 0:
                    oddEven += 1
                if evenOdd > 0:
                    evenOdd += 1
                ans = max(ans, evenOdd, oddEven)
                break
            if (i % 2 != 0 and arr[i] > arr[i+1]) or (i % 2 == 0 and arr[i] < arr[i+1]):
                oddEven += 1
            else:
                oddEven = 0
            if (i % 2 == 0 and arr[i] > arr[i+1]) or (i % 2 != 0 and arr[i] < arr[i+1]):
                evenOdd += 1
            else:
                evenOdd = 0
            ans = max(ans, evenOdd, oddEven)
        return ans