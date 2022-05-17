class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum([1 if op in ['++X','X++'] else -1 for op in operations ])