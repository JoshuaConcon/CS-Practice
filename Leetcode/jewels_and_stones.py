class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel_set = set(J)
        jewel_count = 0
        for stone in S:
            if(stone in jewel_set):
                jewel_count += 1
        return jewel_count
