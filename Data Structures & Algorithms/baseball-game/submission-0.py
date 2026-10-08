class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        scores = []
        for op in operations:
            if op == '+':
                score += scores[-1] + scores[-2]
                scores.append(scores[-1] + scores[-2])
            elif op == 'D':
                score += scores[-1] * 2
                scores.append(scores[-1] * 2)
            elif op == 'C':
                score -= scores.pop()
            else:
                score += int(op)
                scores.append(int(op))
        return score
