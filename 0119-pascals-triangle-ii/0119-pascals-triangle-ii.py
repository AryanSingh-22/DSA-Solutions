class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        
        for i in range(rowIndex):
            new_row = [1]  # every row starts with 1
            for j in range(len(row) - 1):
                new_row.append(row[j] + row[j + 1])  # sum of two above
            new_row.append(1)  # every row ends with 1
            row = new_row
        
        return row