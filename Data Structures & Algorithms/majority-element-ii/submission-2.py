class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        thres = len(nums) // 3
        num1 = None
        num2 = None
        for e in nums:
            if not num1:
                num1 = [e, 1]
                continue
            if not num2:
                num2 = [e, 1]
                continue

            if num1[0] != e:
                num1[1] -= 1
                if num1[1] == 0:
                    num1 = [e, 1]
            elif num1[0] == e:
                num1[1] += 1
                continue
            
            if num2[0] != e:
                num2[1] -= 1
                if num2[1] == 0:
                    num2 = [e, 1]
            elif num2[0] == e:
                num2[1] += 1
                continue


        num1[1] = 0
        num2[1] = 0

        for e in nums:
            if num1[0] == e:
                num1[1] += 1
            if num2[0] == e:
                num2[1] += 1
        
        ans = []
        if num1[1] > thres:
            ans.append(num1[0])
        if num2[1] > thres and num2[0] != num1[0]:
            ans.append(num2[0])

        return ans

            