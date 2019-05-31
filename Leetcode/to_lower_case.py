def convert_char_to_lower(char: str) -> str:
    # ascii values are the following
    # a-z are 97-122
    # A-Z are 65-90
    # diff by 32
    result = char
    char_ascii = ord(char)
    if(char_ascii in range(65,90)):
        # upper case (lol)
        result = chr(char_ascii + 32)
    return result
        

class Solution:
    def toLowerCase(self, str: str) -> str:
        str_list = list(str)
        lowercase_str_list = [ convert_char_to_lower(char) for char in str_list ]
        result = ''.join(lowercase_str_list)
        return result
