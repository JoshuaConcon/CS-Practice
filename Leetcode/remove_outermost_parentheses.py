class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ""
        prev_level = 0
        curr_level = -1
        beginning_index = 0
        for i in range(len(S)):
            prev_level = curr_level
            if(S[i] == '('):
                curr_level += 1
            elif(S[i] == ')'):
                curr_level -= 1
            # if beginning of new section
            if((curr_level == 0) and (prev_level == -1)):
                beginning_index = i+1
            # if end of section
            elif((curr_level == -1) and (prev_level == 0)):
                end_index = i
                subset = S[beginning_index:end_index]
                result = result + subset
        return result
