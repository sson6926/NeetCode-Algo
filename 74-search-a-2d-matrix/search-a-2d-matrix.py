class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return target in [i for row in matrix for i in row]