class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        top = 0
        bottom = row - 1

        while top<=bottom:
            mid = (top + bottom)//2
            if target > matrix[mid][-1]:
                top = mid +1
            elif target < matrix[mid][0]:
                bottom = mid -1 
            else:
                break
        
        if not (top<=bottom): # if no valid row is found
            return False

        row_mid = (top+bottom)//2 
        l = 0
        r = col -1
        while l<=r:
            col_mid = (l+r)//2
            if target > matrix[row_mid][col_mid]:
                l= col_mid +1
            elif target < matrix[row_mid][col_mid]:
                r = col_mid -1 
            else:
                return True
        return False


        