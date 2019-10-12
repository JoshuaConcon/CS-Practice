def isGoodString(word, chars):
    charsLeft = list(word)
    for char in chars:
        if(char in charsLeft):
            charsLeft.pop(charsLeft.index(char))
    return (charsLeft == [])

def getGoodStringLength(word, chars):
    if(isGoodString(word, chars)):
        return len(word)
    else:
        return 0
    

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum([ getGoodStringLength(word, chars) for word in words ])
