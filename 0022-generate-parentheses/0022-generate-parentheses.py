class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current, open_count, close_count):
            # Base case: used up all 2n characters
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Choice 1: add an opening bracket, if we haven't used all n yet
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # Choice 2: add a closing bracket, only if it won't break validity
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return result